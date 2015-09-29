# encoding: utf-8
import uuid
from functools import wraps
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .forms import RegisterForm
from .models import Student, Test, Question, Variant, TestResult
from .lib import nodeproxy


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
                return logout(request)
        else:
            return HttpResponseRedirect("/")

    return wrap


@csrf_protect
def index(request):
    current_student = request.session.get('student', None)

    if current_student:
        return HttpResponseRedirect("/tests/")

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            messages.error(request, u"Форма заполнена не верно")
            return render(request, 'exam/register.html', dict(form=RegisterForm))

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
        return render(request, 'exam/register.html', dict(form=RegisterForm))


@csrf_protect
@check_student
def choose_test(request):
    current = request.session.get('current_test', None)
    if current:
        return HttpResponseRedirect('/tests/%s/' % current)

    tests = Test.objects.filter(disabled=False).order_by('priority')

    return render(request, "exam/test-choose.html", dict(
        student=request.student,
        tests=tests,
    ))


def cleanup(request):
    for k in ('current_test_questions', 'current_test_question', 'current_test', 'uuid'):
        if k in request.session:
            request.session.pop(k)


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
        request.session['uuid'] = str(uuid.uuid4())
    elif current and int(current) != test_id:
        return HttpResponseRedirect('/tests/%s/' % current)
    else:
        test = Test.objects.get(id=request.session['current_test'])

    result, is_new = TestResult.objects.get_or_create(
        session=request.session['uuid'],
        student=request.student,
        test=test,
    )

    questions = request.session['current_test_questions']

    if request.method == 'POST':
        question = Question.objects.get(id=questions[request.session['current_test_question']])

        if question.type == 0:
            if 'variant' not in request.POST:
                messages.error(request, u"Выберите вариант ответа.")

                return render(request, 'exam/test-start.html', dict(
                    test=test,
                    question=question,
                    position=(request.session['current_test_question'] + 1),
                    questions_len=len(questions)
                ))

            answer = int(request.POST['variant'])
        elif question.type == 1:
            answer = [int(i) for i in request.POST['variant']]
        elif question.type == 2:
            answer = request.POST['text']

        variant = Variant.objects.get(id=answer)

        result.answers.append({
            'question': question.id,
            'answer': variant.value,
        })

        result.save()

        request.session['current_test_question'] += 1

    if len(questions) <= request.session['current_test_question']:
        cleanup(request)
        result.gen_result()
        return render(request, "test-finished.html", dict(student=request.student))

    try:
        questions = request.session['current_test_questions']
        question = Question.objects.get(id=questions[request.session['current_test_question']])
        position = request.session['current_test_question']
    except Test.DoesNotExist:
        cleanup(request)

        return HttpResponseRedirect("/tests/")

    return render(request, 'exam/test-start.html', dict(
        test=test,
        question=question,
        position=(position + 1),
        questions_len=len(questions),
        student=request.student,
    ))


def logout(request):
    request.session.clear()
    return HttpResponseRedirect("/")


@staff_member_required
def results(request, result_id):
    try:
        return render(request, 'exam/test-results.html', dict(
            result=TestResult.objects.get(id=int(result_id))
        ))
    except:
        raise Http404