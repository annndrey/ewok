# encoding: utf-8
# Register your models here.
from django.contrib import admin
from .models import Test, Question, Variant, TestResult


class DeleteNotAllowedModelAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False


class VariantsChouces(admin.StackedInline):
    model = Variant
    extra = 1


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
    fieldsets = [
        (None, {'fields': ['timestamp', 'student', 'test', 'result', 'answers']}),
    ]
    readonly_fields = ('timestamp', 'student', 'test', 'answers', 'result')
    list_display = ('timestamp', 'student', 'test')
    list_filter = ('timestamp', 'student', 'test', 'student__group')

    def save_model(self, request, obj, form, change):
        obj.gen_result()
