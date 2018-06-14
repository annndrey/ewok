# encoding: utf-8

import psycopg2
import sqlalchemy
import csv
import pandas as pd
from numpy import nanmean
from StringIO import StringIO
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from django import forms
from django.http import HttpResponse, StreamingHttpResponse
from django.contrib import admin
from django.db.models import Count
from .models import Test, Question, Variant, TestResult, Student, StudentGroup, Teacher
from .forms import TeacherForm


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    con = sqlalchemy.create_engine(url, client_encoding='utf8')
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    return con, meta


def meanrow(row):
    numvalues = []
    for x in row:
        try:
            numvalues.append(float(x))
        except:
            pass
    if len(numvalues) > 0:    
        return nanmean(numvalues)
    else:
        return None

    
def get_group_results(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename="groupresults.csv"'
    writer = csv.writer(response)
    con, meta = connect('exam', 'exam', 'exam')
    Session = sessionmaker(bind=con)
    session = Session()
    tests = meta.tables['exam_test']
    students = meta.tables['exam_student']
    groups = meta.tables['exam_studentgroup']
    testresults = meta.tables['exam_testresult']
    groupnames = [g.name for g in queryset.all()]
    version = "v2"
    # V1
    if version == "v1":
        allresults = session.query(students.c.surname, students.c.name, students.c.middlename, tests.c.title, testresults.c.result, groups.c.name).filter(groups.c.name.in_(groupnames)).join(testresults).join(tests).join(groups)
        outcsv = []
        for i, r in enumerate(allresults):
            for k in r[4].keys():
                row = u"""{0} {1} {2};{5};Тест "{3}";{4}""".format(r[0], r[1], r[2], r[3], (u"%s;%.2f" % (k, r[4][k]) if isinstance(r[4][k], int) else u"%s;%s" % (k,r[4][k].values()[0])), r[5])
                outcsv.append(row)
        outcsv = "\n".join(outcsv)
                
        df = pd.read_csv(StringIO(outcsv), sep=';', header=None, names=['name', 'group', 'test', 'resname', 'resvalue'])
        cols = ['test', 'name', 'group', 'resname', 'resvalue']
        df = df[cols]
        dfgroupped = df.groupby(['test', 'resname', 'group', 'name'])['resvalue'].sum().unstack(['group', 'name'])
        summary_ave_data = dfgroupped.copy()
        summary_ave_data['average'] = summary_ave_data.apply(meanrow, axis=1)
    # V2
    else:
        allresults = session.query(students.c.surname, students.c.name, students.c.middlename, tests.c.title, testresults.c.answers, testresults.c.result, groups.c.name).filter(groups.c.name.in_(groupnames)).join(testresults).join(tests).join(groups)
        rowlist = []
        for r in allresults:
            questions = {}
            answers = {}
            for q in sorted(r[5].keys(), key=lambda x: int(x)):
                questions[q] = r[5][q]
            for q in questions.keys():
                for a in questions[q]:
                    if a not in answers.keys():
                        answers[a] = questions[q][a]
                    else:
                        answers[a] = answers[a] + questions[q][a]
            for a in answers.keys():
                rowlist.append([" ".join(r[0:3]), r[6], r[3], a, answers[a]])
            #for a in questions[q]:
            #    rowlist.append([" ".join(r[0:3]), r[6], r[3], q, a, questions[q][a]])
            
        outdf = pd.DataFrame(rowlist)
        # outdf = pd.read_sql(allresults.statement, con)

        cls = ['name', 'group', 'test', 'parameter', 'value']
        outdf.columns = cls
        outdf = outdf[['test', 'name', 'group', 'parameter', 'value']]
        # print outdf
        summary_ave_data = outdf.groupby(['test', 'name', 'group', 'parameter'])['value'].sum().unstack(['group', 'parameter']).fillna(0)
        # summary_ave_data['average'] = summary_ave_data.apply(nanmean, axis=1)
        summary_ave_data['sum'] = summary_ave_data.apply(sum, axis=1)

    summary_ave_data.to_csv(response , sep=';', encoding='utf-8', float_format='%g')
    
    return response
    
get_group_results.short_description = "Скачать результаты"


class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return True
        #return False


class VariantsChouces(admin.StackedInline):
    model = Variant
    extra = 0

class QuestionChoices(admin.StackedInline):
    model = Question
    extra = 0
    max_num = 0
    show_change_link = 1
    readonly_fields = ('description', 'type')
    can_delete = False
    ordering = ('number',)

    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm
    list_display = ['user', 'get_all_groups']#'get_all_groups']
    list_filter = ['user', ]#'get_all_groups']
    search_fields = ['user__username', 'user__first_name', 'user__last_name']

    #def get_queryset(self, request):
    #    qs = super(TeacherAdmin, self).get_queryset(request)
    #    return qs.filter(stgroup__teacher__count__gt=0)
    
    def get_all_groups(self, obj):
        return "; ".join([g.name for g in obj.stgroup.all()])

    get_all_groups.short_description = 'Группы'

    def get_groups(self, obj):
        return obj.stgroup.name
    def get_fname(self, obj):
        return obj.user.first_name
    def get_lname(self, obj):
        return obj.user.last_name

    
@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'stcount')
    list_filter = ('name',)
    actions = [get_group_results,]

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # fields = ['title', 'questions']
    fieldsets = [
        (None, {'fields': ['disabled', 'name', 'title', 'description', 'timeout', 'func', 'priority']}),
    ]

    inlines = (QuestionChoices,)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['test', 'type', 'number', 'description']}),
    ]

    list_display = ['__unicode__', 'test']
    list_editable = ['test']
    list_filter = ['test', 'type']

    inlines = (VariantsChouces,)


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):

    def result_link(self, obj):
        return '<a href="/results/view/{0.id}">Просмотр результатов</a>'.format(obj)

    class Media:
        js = ('custom.js',)

    result_link.allow_tags = True
    result_link.short_description = u'Результаты'

    readonly_fields = ('timestamp', 'student', 'test', 'result_link')
    exclude = ['answers', 'result']

    list_display = ('timestamp', 'student', 'test')
    list_filter = ('timestamp', 'student', 'test', 'student__name', 'student__stgroup')
    search_fields = ('student__surname',)
    
    def save_model(self, request, obj, form, change):
        obj.gen_result()


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('surname', 'name', 'middlename', 'age', 'sex')
    list_display = ('stgroup', 'surname', 'name', 'middlename', 'age', 'sex')
    list_filter = ('stgroup', 'surname', 'name', 'middlename', 'age', 'sex')
    search_fields = ('surname',)
    class Media:
        js = ('custom.js',)
        
