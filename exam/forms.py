#!/usr/bin/env python
# encoding: utf-8
from django import forms
from .models import Student


class RegisterForm(forms.Form):
    surname = forms.CharField(label=u'Фамилия', max_length=100)
    name = forms.CharField(label=u'Имя', max_length=100, )
    middlename = forms.CharField(label=u'Отчество', max_length=100)
    group = forms.CharField(label=u'Группа', max_length=100)
    age = forms.IntegerField(initial=16, label=u"Возраст", min_value=15, max_value=125)
    sex = forms.ChoiceField(choices=Student.GENDER.items(), label=u"Пол")
