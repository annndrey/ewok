#!/usr/bin/env python
# encoding: utf-8
from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label=u'Имя', max_length=100)
    middlename = forms.CharField(label=u'Отчество', max_length=100)
    surname = forms.CharField(label=u'Группа', max_length=100)
