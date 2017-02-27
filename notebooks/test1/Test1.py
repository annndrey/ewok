
# coding: utf-8

# In[1]:

import json

questions = json.load(open('questions.json'))


# In[2]:

import datetime
import sys, os

sys.path.append('/srv/ewok/ewok/settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'production'

import django
django.setup()

from exam.models import *


# In[3]:

test, is_new = Test.objects.get_or_create(title=u"Тест №1")

for c, question in enumerate(questions):
    que, variants = question
    q, is_new = Question.objects.get_or_create(test=test, description=que, number=(c + 1), type=0)

    for variant in variants:
        desc, value = variant
        Variant.objects.get_or_create(question=q, text=desc, value=value)


# In[ ]:



