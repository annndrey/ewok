# encoding: utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm, ChooseTestForm
from .models import Student


@cache_page(300)
@csrf_protect
def index(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'register.html', dict(form=RegisterForm))

        student_data = {
            'gender': form['gender'].data,
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
        return render(request, 'register.html', dict(form=RegisterForm))


@csrf_protect
def choose_test(request):
    return render(request, "test-choose.html", dict(form=ChooseTestForm))