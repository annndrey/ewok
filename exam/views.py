# encoding: utf-8
import datetime
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm, ChooseTestForm
from .models import Student


@csrf_protect
def index(request):
    current_student = request.session.get('student', None)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'register.html', dict(form=RegisterForm))

        student_data = {
            'sex': form['sex'].data,
            'name': form.cleaned_data['name'],
            'surname': form.cleaned_data['surname'],
            'middlename': form.cleaned_data['middlename'],
            'age': form.cleaned_data['age'],
            'group': form.cleaned_data['group']
        }

        student, is_new = Student.objects.get_or_create(**student_data)

        request.session['student'] = student.pk

        return HttpResponseRedirect("/tests/")
    elif request.method == 'GET':
        if current_student:
            return HttpResponseRedirect("/tests/")
        return render(request, 'register.html', dict(form=RegisterForm))


@csrf_protect
def choose_test(request):
    student = request.session.get('student', None)
    if not student:
        return HttpResponseRedirect("/")

    return render(request, "test-choose.html", dict(form=ChooseTestForm))