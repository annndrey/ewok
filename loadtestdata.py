#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import datetime
import django

testtitle=u'%s' % sys.argv[1].decode('utf-8')
testdata=open(sys.argv[2]).read()
vals = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
d = (i.decode('utf-8').split("$$") for i in testdata.split('±'))
questions = [[q.strip(), [i.strip() for i in a.strip().split('\n')]] for q, a in d]

django.setup()

from exam.models import *
tdescr = u"""Прочитайте утверждения. По шкале от 0 до 10 оцените степень своего согласия с утверждениями.

0 – это совершенно не так
10 – это именно так"""

test, is_new = Test.objects.get_or_create(name=testtitle, title=testtitle, description=tdescr)

for idx, item in enumerate(questions):
    text, variants = item
    print text, variants
    q, is_new = Question.objects.get_or_create(test=test, description=text, number=(idx+1), type=0)

    for value, variant in enumerate(variants):
        Variant.objects.get_or_create(question=q, text=variant, value={value+1: value+1})
