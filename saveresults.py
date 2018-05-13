#!/usr/bin/env python
# encoding: utf-8

import pprint
import psycopg2
import sqlalchemy
import pandas as pd
from numpy import nanmean
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from StringIO import StringIO
pp = pprint.PrettyPrinter(indent=4)

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

restosave = ['Общежитие', "Учебный процесс"]
#restosave = ["Учебный процесс"]

#restosave = ["Тест №2", "Тест №3"]
allresults = session.query(students.c.surname, students.c.name, students.c.middlename, tests.c.title, testresults.c.answers, testresults.c.result, groups.c.name).filter(tests.c.title.in_(restosave)).join(testresults).join(tests).join(groups).limit(8)
rowlist = []

for r in allresults:
    row = {"name":"", "group":"", "test":""}
    rescoeffs = {}

    pp.pprint(r[5])
    
    for k in sorted(r[5].keys(), key=lambda x: int(x)):
        rescoeffs[k] = r[5][k].values()[0]
        
            
    row['name'] = " ".join(r[0:3])
    row['group'] = r[6]
    row['test'] = r[3]

    for rk in rescoeffs.keys():
        if rk not in row.keys():
            row[rk] = rescoeffs[rk]

    print row
    rowlist.append(row)


outdf = pd.DataFrame(rowlist)
cls = ['name', 'group', 'test']
cols = sorted([c for c in outdf.columns.tolist() if c not in cls], key=lambda x: int(x))
outdf = outdf[cls + cols]
print outdf

# это для тестов, выгружается в админке, в группах
