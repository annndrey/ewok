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
# restosave = ['Общежитие', "Учебный процесс", "Тест №2", "Тест №3"]
#restosave = ["Учебный процесс"]
restosave = ["Общежитие"]
#restosave = ["Тест №2", "Тест №3"]
#restosave = ["Тест №2",]

def v2():
    allresults = session.query(students.c.surname, students.c.name, students.c.middlename, tests.c.title, testresults.c.answers, testresults.c.result, groups.c.name).filter(tests.c.title.in_(restosave)).join(testresults).join(tests).join(groups).limit(2)

    rowlist = []
    for r in allresults:
        questions = {}
        answers = {}
        for q in sorted(r[5].keys(), key=lambda x: int(x)):
            questions[q] = r[5][q]
        for q in questions.keys():
            for a in questions[q]:
                if a not in answers.keys():
                    answers[a] = questions[q][a]
                else:
                    answers[a] = answers[a] + questions[q][a]
        for a in answers.keys():
            rowlist.append([" ".join(r[0:3]), r[6], r[3], a, answers[a]])
            #for a in questions[q]:
            #    rowlist.append([" ".join(r[0:3]), r[6], r[3], q, a, questions[q][a]])
            
    outdf = pd.DataFrame(rowlist)
    # outdf = pd.read_sql(allresults.statement, con)

    cls = ['name', 'group', 'test', 'parameter', 'value']
    outdf.columns = cls
    outdf = outdf[['test', 'name', 'group', 'parameter', 'value']]
    # print outdf
    groupped = outdf.groupby(['test', 'name', 'group', 'parameter'])['value'].sum().unstack(['group', 'parameter']).fillna(0)
    groupped['average'] = groupped.apply(nanmean, axis=1)
    groupped['sum'] = groupped.apply(sum, axis=1)
    print groupped
    # outdf = outdf.groupby(['name', 'group', 'test', 'question'])
    #outdf = pd.pivot_table(outdf, index=['group', 'name', 'test'], columns='parameter', values='value', aggfunc='first')
    #outdf = outdf.reset_index()
    #params = [x for x in outdf.columns if x not in cls]
    #outdf['sum'] = outdf[params].sum(axis=1)

def v1():
    allresults = session.query(students.c.surname, students.c.name, students.c.middlename, tests.c.title, testresults.c.result, groups.c.name).filter(tests.c.title.in_(restosave)).join(testresults).join(tests).join(groups).limit(2)
    outcsv = []
    for i, r in enumerate(allresults):
        for k in r[4].keys():
            row = u"""{0} {1} {2};{5};{3};{4}""".format(r[0], r[1], r[2], r[3], (u"%s;%.2f" % (k, r[4][k]) if isinstance(r[4][k], int) else u"%s;%s" % (k,r[4][k].values()[0])), r[5])
            outcsv.append(row)
    outcsv = "\n".join(outcsv)
                
    df = pd.read_csv(StringIO(outcsv), sep=';', header=None, names=['name', 'group', 'test', 'resname', 'resvalue'])
    cols = ['test', 'name', 'group', 'resname', 'resvalue']
    df = df[cols]
    dfgroupped = df.groupby(['test', 'resname', 'group', 'name'])['resvalue'].sum().unstack(['group', 'name'])

    summary_ave_data = dfgroupped.copy()
    summary_ave_data['average'] = summary_ave_data.apply(meanrow, axis=1)
    print summary_ave_data

if __name__ == "__main__":
    v2()
