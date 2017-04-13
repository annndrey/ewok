#!/usr/bin/env python
# encoding: utf-8

import psycopg2
import sqlalchemy
import pandas as pd
from numpy import nanmean
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from StringIO import StringIO

def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con, meta

def meanrow(row):
    numvalues = []
    for x in row:
        try:
            numvalues.append(float(x))
        except:
            pass
    if len(numvalues) > 0:    
        return nanmean(numvalues)
    else:
        return None
    
con, meta = connect('exam', 'exam', 'exam')
Session = sessionmaker(bind=con)
session = Session()
tests = meta.tables['exam_test']
students = meta.tables['exam_student']
groups = meta.tables['exam_studentgroup']
testresults = meta.tables['exam_testresult']

allresults = session.query(students.c.surname, students.c.name, students.c.middlename, tests.c.title, testresults.c.result, groups.c.name).filter(tests.c.title.in_(('Общежитие', "Учебный процесс"))).join(testresults).join(tests).join(groups)
outcsv = []
for i, r in enumerate(allresults):
    for k in r[4].keys():
        ##r[4][k] = r[4][k].values()[0]
        #print r[4][k].values()
        #print ("%s;%.2f" % (k, r[4][k]) if isinstance(r[4][k], int) else "%s;%s" % (k,r[4][k].values()[0]))
        outcsv.append(u"""{0} {1} {2};{5};Тест "{3}";{4}""".format(r[0], r[1], r[2], r[3], ("%s;%.2f" % (k, r[4][k]) if isinstance(r[4][k], int) else "%s;%s" % (k,r[4][k])), r[5]))
        
outcsv = "\n".join(outcsv)

df = pd.read_csv(StringIO(outcsv), sep=';', header=None, names=['name', 'group', 'test', 'resname', 'resvalue'])
cols = ['test', 'name', 'group', 'resname', 'resvalue']
df = df[cols]
dfgroupped = df.groupby(['test', 'resname', 'group', 'name'])['resvalue'].sum().unstack(['group', 'name'])
summary_ave_data = dfgroupped.copy()
summary_ave_data['average'] = summary_ave_data.apply(meanrow, axis=1)
summary_ave_data.to_excel('alldatafromdb_12.04.17.xlsx')
summary_ave_data.to_csv('alldatafromdb_12.04.17.csv', sep=';')

#dfgroupped.to_csv('alldatafromdb_12.04.csv', sep=';')
