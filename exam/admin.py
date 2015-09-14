# encoding: utf-8
# Register your models here.
from django.contrib import admin
from .models import Test, Question, Variant


class QuestionChouces(admin.StackedInline):
    model = Variant
    extra = 1


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    # fields = ['title', 'questions']
    fieldsets = [
        (None, {'fields': ['disabled', 'title', 'timeout', 'func', 'priority']}),
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['test', 'type', 'number', 'description']}),
    ]

    list_display = ['__unicode__', 'test']

    inlines = (QuestionChouces,)


# @admin.register(QuestionVariant)
# class QuestionVariantAdmin(admin.ModelAdmin):
#     pass
