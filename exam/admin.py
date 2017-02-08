# encoding: utf-8
# Register your models here.

from django.contrib import admin
from django.db.models import Count
from .models import Test, Question, Variant, TestResult, Student, StudentGroup, Teacher


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
    list_display = ['user', 'stgroup']
    list_filter = ['user', 'stgroup']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'stgroup__name']

    def get_fname(self, obj):
        return obj.user.first_name
    
    def get_lname(self, obj):
        return obj.user.last_name
    
    def get_stgroupname(self, obj):
        return obj.stgroup.name

@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'stcount')
    list_filter = ('name',)

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
        
