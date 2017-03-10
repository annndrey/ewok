#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Student, StudentGroup, Teacher


class RegisterForm(forms.Form):
    surname = forms.CharField(label=u'Фамилия', max_length=100)
    name = forms.CharField(label=u'Имя', max_length=100, )
    middlename = forms.CharField(label=u'Отчество', max_length=100)
    stgroup = forms.ModelChoiceField(queryset=StudentGroup.objects, to_field_name="name", label=u'Группа')
    teacher = forms.ModelChoiceField(queryset=Teacher.objects, to_field_name="user", label=u'Преподаватель')
    age = forms.IntegerField(initial=16, label=u"Возраст", min_value=15, max_value=125)
    sex = forms.ChoiceField(choices=Student.GENDER.items(), label=u"Пол")
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Teacher.objects.filter(user__is_active=True)
        self.fields['stgroup'].queryset = StudentGroup.objects.exclude(id=4)
        
class SignupForm(forms.Form):
    lname = forms.CharField(label=u'Фамилия', max_length=100)
    fname = forms.CharField(label=u'Имя', max_length=100, )
    middlename = forms.CharField(label=u'Отчество', max_length=100)
    login = forms.CharField(label=u'Логин', max_length=100)
    password = forms.CharField(label=u'Пароль', max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField(label=u'email', max_length=100)

class LoginForm(forms.Form):
    username = forms.CharField(label=u'username', max_length=100)
    password = forms.CharField(label=u'Пароль', max_length=100, widget=forms.PasswordInput)

class AcceptForm(forms.Form):
    accept = forms.BooleanField(label=u'Да, разрешаю использовать мои персональные данные')
