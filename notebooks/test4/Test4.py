
# coding: utf-8

# In[4]:

import json

template = [
    'ostentatiously',
    'effectiveness',
    'uniqueness',
    'insolvency',
    'social_pessimism',
    'breakdown_cultural_barriers',
    'maximalism',
    'time_perspective',
    'nosuicide_factor',
]


data = [[None, None] for i in xrange(29)]

with open('test_coeff.csv') as f:
    for fidx, i in enumerate(f):
        result = {}

        if not i:
            continue

        vals = i.split(',')
        for idx, key in enumerate(template):
            result[key] = float(vals[idx])

        data[int(fidx/2)][0 if (fidx % 2) == 0 else 1] = result

data = zip([i.strip("\n\r") for i in open('Test4.aspx')], data)


# In[5]:

import datetime
import django
django.setup()

from exam.models import *


# In[6]:

test, is_new = Test.objects.get_or_create(title=u"Суицидальный риск")

c = 1
for question, variant in data:
    positive, negative = variant
    q, is_new = Question.objects.get_or_create(test=test, description=question, number=c, type=0)

    Variant.objects.get_or_create(question=q, text=u"Да", value=positive)
    Variant.objects.get_or_create(question=q, text=u"Нет", value=negative)

    c += 1


# In[ ]:



