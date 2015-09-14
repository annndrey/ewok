# encoding: utf-8
from functools import wraps
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
        except Student.DoesNotExist:
            student = None

        if student:
            request.student = student
            return func(request, *args, **kwargs)
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


@check_student
def start_test(request, test_id):
    test_id = int(test_id)
    current = request.session.get('current_test', None)

    if not current:
        try:
            test = Test.objects.get(disabled=False, id=test_id)
            request.session['current_test'] = test.pk
            questions = [q.id for q in test.question_set.all().order_by('?')]
            request.session['current_test_questions_ordering'] = questions
            request.session['current_test_question'] = questions[0]
        except Test.DoesNotExist:
            return Http404()
        except:
            return HttpResponseGone()

    elif current and int(current) != test_id:
        return HttpResponseRedirect('/tests/%s/' % current)

    test = Test.objects.get(id=request.session['current_test'])
    questions = request.session['current_test_questions_ordering']
    question = request.session['current_test_question']
    position = questions.index(question)

    if request.method == 'POST':
        pass

    question = Question.objects.get(id=question)

    return render_to_response('test-start.html', dict(
        test=test,
        question=question,
        position=(position + 1),
        questions_len=len(questions)
    ))
