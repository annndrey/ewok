#!/usr/bin/env python
# encoding: utf-8
import json
from django import forms
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.html import format_html
from jsonfield.utils import default
from .models import Student


class RegisterForm(forms.Form):
    surname = forms.CharField(label=u'Фамилия', max_length=100)
    name = forms.CharField(label=u'Имя', max_length=100, )
    middlename = forms.CharField(label=u'Отчество', max_length=100)
    group = forms.CharField(label=u'Группа', max_length=100)
    age = forms.IntegerField(initial=10, label=u"Возраст", min_value=0, max_value=125)
    sex = forms.ChoiceField(choices=Student.GENDER.items(), label=u"Пол")


class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is None:
            value = ""
        if not isinstance(value, basestring):
            value = json.dumps(value, indent=2, default=default, ensure_ascii=False)

        try:
            val = json.loads(value) if isinstance(value, basestring) else value
            if not isinstance(value, dict):
                val = None
        except:
            val = None

        return render_to_string('json_widget.html', dict(
            value=val,
            name=name,
            json=json.dumps(value)
        ))
        # return super(JSONWidget, self).render(name, value, attrs)
