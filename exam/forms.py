#!/usr/bin/env python
# encoding: utf-8
from django import forms
from .models import Student, StudentGroup


class RegisterForm(forms.Form):
    surname = forms.CharField(label=u'Фамилия', max_length=100)
    name = forms.CharField(label=u'Имя', max_length=100, )
    middlename = forms.CharField(label=u'Отчество', max_length=100)
    stgroup = forms.ModelChoiceField(queryset=StudentGroup.objects, to_field_name="name", label=u'Группа')
    age = forms.IntegerField(initial=16, label=u"Возраст", min_value=15, max_value=125)
    sex = forms.ChoiceField(choices=Student.GENDER.items(), label=u"Пол")

