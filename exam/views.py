# encoding: utf-8
from functools import wraps
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseGone
from django.shortcuts import render_to_response
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_protect
from .forms import RegisterForm
from .models import Student, Test, Question


def check_student(func):
    @wraps(func)
    def wrap(request, *args, **kwargs):
        student = request.session.get('student', None)
        try:
            student = Student.objects.get(id=int(student))
        except:
            student = None

        if student:
            request.student = student
            try:
                return func(request, *args, **kwargs)
            except ObjectDoesNotExist:
                raise Http404()
        else:
            return HttpResponseRedirect("/")

    return wrap


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
@check_student
def choose_test(request):
    current = request.session.get('current_test', None)
    if current:
        return HttpResponseRedirect('/tests/%s/' % current)

    tests = Test.objects.filter(disabled=False).order_by('priority')

    return render(request, "test-choose.html", dict(tests=tests))


@csrf_protect
@check_student
def start_test(request, test_id):
    test_id = int(test_id)
    current = request.session.get('current_test', None)

    if not current:
        test = Test.objects.get(disabled=False, id=test_id)
        request.session['current_test'] = test.pk
        questions = [q.id for q in test.question_set.all().order_by('number')]
        request.session['current_test_questions'] = questions
        request.session['current_test_question'] = 0
    elif current and int(current) != test_id:
        return HttpResponseRedirect('/tests/%s/' % current)

    try:
        test = Test.objects.get(id=request.session['current_test'])
        questions = request.session['current_test_questions']
        question = Question.objects.get(id=questions[request.session['current_test_question']])
        position = question + 1
    except Test.DoesNotExist:
        for k in ('current_test_questions', 'current_test_question', 'current_test'):
            if k in request.session:
                request.session.pop(k)

        return HttpResponseRedirect("/tests/")

    if request.method == 'POST':
        if question.type == 0:
            answer = int(request.POST['variant'][0])
        elif question.type == 1:
            answer = [int(i) for i in request.POST['variant']]
        elif question.type == 2:
            answer = request.POST['text']

    return render(request, 'test-start.html', dict(
        test=test,
        question=question,
        position=(position + 1),
        questions_len=len(questions)
    ))
