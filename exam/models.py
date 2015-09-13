# encoding: utf-8
from django.core.exceptions import ValidationError
from jsonfield import JSONField
import re
from exam.lib.nodeproxy import execute
from django.db import models
from redactor.fields import RedactorField

TAG_RE = re.compile(r'<[^>]+>')

default_func = '''function (answers) {
    var result = [];
    answers.map(function (answer) {
        result.push(answer);
    });
    return result;
}'''


def remove_tags(text):
    return TAG_RE.sub('', text)


class Test(models.Model):
    title = models.CharField(max_length=255, verbose_name=u"Название")
    func = models.TextField(blank=False, default=default_func)
    timeout = models.TimeField(verbose_name=u"Максимальное время выполнения")

    class Meta:
        verbose_name = u"Тест"
        verbose_name_plural = u"Тесты"

    def __unicode__(self):
        return u"{0.title}".format(self)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        execute(self.func, args=[[]])
        return super(Test, self).save()


class Question(models.Model):
    TYPES = {
        0: u"Один из вариантов ответа",
        1: u"Несколько вариантов ответа",
        2: u"Ответ в свободной форме",
    }

    test = models.ForeignKey("Test")
    description = RedactorField(verbose_name=u"Описание")
    type = models.PositiveSmallIntegerField(choices=TYPES.items(), db_index=True, verbose_name=u"Тип")

    class Meta:
        verbose_name = u"Вопрос"
        verbose_name_plural = u"Вопросы"

    def __unicode__(self):
        return u"{0}".format(remove_tags(self.description).strip(" "))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.type == 2 and self.variant_set:
            raise ValidationError(u"У ответа в свободной форме не может быть")

        return super(Question, self).save()


class Variant(models.Model):
    question = models.ForeignKey('Question')
    text = models.CharField(max_length=512, verbose_name=u"Вариант ответа")
    value = JSONField(verbose_name=u"Коэффициент")

    class Meta:
        verbose_name = u"Вариант ответа"
        verbose_name_plural = u"Варианты ответов"

    def __unicode__(self):
        return u"({0.value}) {0.text}".format(self)


class Student(models.Model):
    GENDER = {
        "male": u"Мужской",
        "female": u"Женский",
    }

    AGES = [(i, i) for i in xrange(0, 125)]

    surname = models.CharField(max_length=60, verbose_name=u"фамилия", db_index=True)
    name = models.CharField(max_length=60, verbose_name=u"имя", db_index=True)
    middlename = models.CharField(max_length=60, verbose_name=u"отчество", db_index=True)
    group = models.CharField(max_length=60, verbose_name=u"группа", db_index=True)
    age = models.PositiveSmallIntegerField(verbose_name=u"возраст", db_index=True, choices=AGES)
    gender = models.PositiveSmallIntegerField(choices=GENDER.items(), db_index=True)

    class Meta:
        unique_together = (
            ('surname', 'middlename', 'name'),
        )

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.name = self.name.strip(' ')
        self.middlename = self.middlename.strip(' ')
        self.surname = self.surname.strip(' ')
        return super(Student, self).save()


class TestResult(models.Model):
    student = models.ForeignKey(Student, verbose_name=u"студент")
    answers = JSONField(verbose_name=u'результаты')
    result = JSONField(verbose_name=u'результаты')
