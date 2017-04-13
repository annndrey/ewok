#!/usr/bin/env python
# encoding: utf-8
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import Student, StudentGroup, Teacher



class RegisterForm(forms.Form):
    surname = forms.CharField(label=u'Фамилия', max_length=100)
    name = forms.CharField(label=u'Имя', max_length=100, )
    middlename = forms.CharField(label=u'Отчество', max_length=100)
    teacher = forms.ModelChoiceField(queryset=User.objects, to_field_name='user', label=u'Преподаватель')
    stgroup = forms.ModelChoiceField(queryset=StudentGroup.objects, label=u'Группа', widget=forms.Select(attrs={'disabled':'disabled'}))
    age = forms.IntegerField(initial=16, label=u"Возраст", min_value=15, max_value=125)
    sex = forms.ChoiceField(choices=Student.GENDER.items(), label=u"Пол")
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['teacher'].queryset = Teacher.objects.filter(user__is_active=True)
        self.fields['stgroup'].queryset = StudentGroup.objects.filter(teacher__user__is_active=True).exclude(id=4)
        
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
    accept = forms.BooleanField(label=u'Да, разрешаю использовать мои персональные данные', required=False, initial=False)
    dummy = forms.CharField(initial='dummy', widget=forms.widgets.HiddenInput())

class TeacherForm(forms.ModelForm):
    stgroup = forms.ModelMultipleChoiceField(queryset=StudentGroup.objects.all(), label='Группы', required=False)

    class Meta:
        model = Teacher
        fields = ['user', 'tests', 'stgroup']

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

        if self.instance.pk is not None:
            self.initial['stgroup'] = [values[0] for values in self.instance.stgroup.values_list('pk')]

    #def save(self, commit=True):
    #    instance = super(TeacherForm, self).save(commit)
    #    def save_m2m():
    #        instance.stgroup = self.cleaned_data['stgroup']

    #    if commit:
    #        save_m2m()
    #    elif hasattr(self, 'save_m2m'):
    #        save_old_m2m = self.save_m2m

    #        def save_both():
    #            save_old_m2m()
    #            save_m2m()

    #        self.save_m2m = save_both
    #    else:
    #        self.save_m2m = save_m2

    #    return instance

    #save.alters_data = True
            
