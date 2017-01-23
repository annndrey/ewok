#!/usr/bin/env python
# encoding: utf-8

import psycopg2

def renamegroup(oldname):
    newname = oldname.strip().decode('utf-8').upper().encode('utf-8').replace(' ', '').replace('-', '')
    return newname

groupsfile = open('groups.csv', 'r')
#standgroups = []
#for g in groupsfile:
#    g = g.replace('\n', '')
#    g = renamegroup(g)
#    if g not in standgroups:
#        standgroups.append(g)


    
conn = psycopg2.connect("dbname='exam' user='exam' host='localhost' password='***'")
cur = conn.cursor()
#for g in standgroups:
#    cur.execute("""insert into exam_studentgroup (name) values ('%s')""" % g)
#    conn.commit()
#cur.close()
#conn.close()
cur.execute("""SELECT id, name, "group" from exam_student""")
rows = cur.fetchall()
cur.execute("""SELECT id, name from exam_studentgroup""")
groups = {}
for g in cur.fetchall():
    groups[g[1]] = g[0]


print groups

rowstr = "{0}|{1} --- {2}|{3}"

for row in rows:
    newname = renamegroup(row[2])
    if newname in groups.keys():
        print rowstr.format(row[0], row[2], groups[newname], newname)
        cur.execute("""update exam_student set stgroup=%s where id=%s""" % (groups[newname], row[0]))
        conn.commit()

cur.close()
conn.close()
