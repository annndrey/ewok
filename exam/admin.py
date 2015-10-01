# encoding: utf-8
# Register your models here.
from django.contrib import admin
from django import forms
from jsonfield import JSONField
from .models import Test, Question, Variant, TestResult, Student


class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


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


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # fields = ['title', 'questions']
    fieldsets = [
        (None, {'fields': ['disabled', 'title', 'description', 'timeout', 'func', 'priority']}),
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
class TestResultAdmin(DeleteNotAllowedModelAdmin):

    def result_link(self, obj):
        return '<a href="/results/view/{0.id}">Просмотр результатов</a>'.format(obj)

    result_link.allow_tags = True
    result_link.short_description = u'Результаты'

    readonly_fields = ('timestamp', 'student', 'test', 'result_link')
    exclude = ['answers', 'result']

    list_display = ('timestamp', 'student', 'test')
    list_filter = ('timestamp', 'student', 'test', 'student__group')

    def save_model(self, request, obj, form, change):
        obj.gen_result()


@admin.register(Student)
class StudentAdmin(DeleteNotAllowedModelAdmin):
    readonly_fields = ('surname', 'name', 'middlename', 'group', 'age', 'sex')
    list_display = ('surname', 'name', 'middlename', 'group', 'age', 'sex')
    list_filter = ('surname', 'name', 'middlename', 'group', 'age', 'sex')

