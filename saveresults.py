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
    con.execution_options(stream_results=True)
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

restosave = ['Общежитие', "Учебный процесс", "Тест №2", "Тест №3"]
# restosave = ["Учебный процесс"]

#restosave = ["Тест №2", "Тест №3"]
#restosave = ["Тест №3",]

allresults = session.query(students.c.surname, students.c.name, students.c.middlename, tests.c.title, testresults.c.answers, testresults.c.result, groups.c.name).filter(tests.c.title.in_(restosave)).join(testresults).join(tests).join(groups)

rowlist = []
for r in allresults:
    questions = {}
    for q in sorted(r[5].keys(), key=lambda x: int(x)):
        questions[q] = r[5][q]
        
    for q in questions.keys():
        for a in questions[q]:
            rowlist.append([" ".join(r[0:3]), r[6], r[3], q, a, questions[q][a]])

outdf = pd.DataFrame(rowlist)
#outdf = pd.read_sql(allresults.statement, con)
#
cls = ['name', 'group', 'test', 'question', 'parameter', 'value']
outdf.columns = cls
outdf = outdf[['test', 'group', 'name', 'question', 'parameter', 'value']]
#outdf = outdf.groupby(['name', 'group', 'test', 'question'])
outdf = pd.pivot_table(outdf, index=['group', 'name', 'test', 'question'], columns='parameter', values='value', aggfunc='first')
outdf = outdf.reset_index()
params = [x for x in outdf.columns if x not in cls]
outdf['sum'] = outdf[params].sum(axis=1)
print outdf
# это для тестов, выгружается в админке, в группах
