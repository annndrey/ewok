# encoding: utf-8
import datetime
from exam.lib import nodeproxy
import re
from jsonfield import JSONField
from exam.lib.nodeproxy import execute
from django.db import models
from django.contrib.auth.models import User
from redactor.fields import RedactorField

TAG_RE = re.compile(r'<[^>]+>')

default_func = '''function (answers) {
    // this.student.sex
    // this.student.age
    var result = {};
    answers.map(function (answer, number) {
        result[number+1] = answer.answer;
    });
    return result;
}'''


def remove_tags(text):
    return TAG_RE.sub('', text)


class StudentGroup(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")
    description = RedactorField(verbose_name=u"Описание", default='', blank=True)
    #teacher = models.ForeignKey("Teacher", verbose_name='Преподаватель', default=1, blank=True, null=True, related_name='+')
    
    def tcount(self):
        if len(self.teacher.all()) > 0:
            return "---"
        return ""

    def stcount(self):
        return len(self.students.all())

    stcount.short_description = u'Число студентов'

    class Meta:
        verbose_name = u"Группа"
        verbose_name_plural = u"Группы"

    def __unicode__(self):
        return u"{1}  {0.name}".format(self, self.tcount())
        
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        return super(StudentGroup, self).save()

class Teacher(models.Model):
    #id = models.AutoField(primary_key=True, default=1)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"учетная запись")
    tests = models.ManyToManyField("Test", verbose_name=u"тесты", related_name='teacher', blank=True)
    stgroup = models.ManyToManyField("StudentGroup", verbose_name='Группы',  blank=True, null=True, related_name='teacher')
    
    class Meta:
        verbose_name = u"Преподаватель"
        verbose_name_plural = u"Преподаватели"

    def __unicode__(self):
        return u"{0} {1}".format(self.user.first_name, self.user.last_name)

    #def save(self, *args, **kwargs):
    #    #if not self.pk:
    #    obj = Teacher()#super(Teacher, self)#.save(*args, **kwargs)
    #    return obj
    #    #obj.user=
    
class Test(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Отображаемое имя")
    title = models.CharField(max_length=255, verbose_name=u"Название")
    func = models.TextField(blank=False, default=default_func)
    timeout = models.TimeField(verbose_name=u"Максимальное время выполнения", default=datetime.time(0,40,0))
    disabled = models.BooleanField(verbose_name=u"Отключен", db_index=True, default=True)
    description = RedactorField(verbose_name=u"Описание", default='', blank=True)
    priority = models.IntegerField(default=1000, verbose_name=u"Приоритет сортировки", db_index=True)

    class Meta:
        verbose_name = u"Тест"
        verbose_name_plural = u"Тесты"

    def __unicode__(self):
        return u"{0.title}".format(self)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        execute(self.func, args=[[]], g={'student': {'age': 99, 'sex': True}})
        return super(Test, self).save()


class Question(models.Model):
    TYPES = {
        0: u"Один из вариантов ответа, вертикально",
        1: u"Несколько вариантов ответа",
        2: u"Ответ в свободной форме",
        3: u"Один из вариантов ответа, горизонтально"
    }

    test = models.ForeignKey("Test")
    number = models.PositiveSmallIntegerField(verbose_name=u'Порядок вопроса')
    description = RedactorField(verbose_name=u"Описание")
    type = models.PositiveSmallIntegerField(choices=TYPES.items(), db_index=True, verbose_name=u"Тип")

    class Meta:
        verbose_name = u"Вопрос"
        verbose_name_plural = u"Вопросы"
        unique_together = (
            ("test", "number"),
        )

    def __unicode__(self):
        return u"{0}".format(remove_tags(self.description).strip(" "))

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # if self.type == 2 and self.variant_set:
        #     raise ValidationError(u"У ответа в свободной форме не может быть")

        return super(Question, self).save()


class Variant(models.Model):
    question = models.ForeignKey('Question')
    text = models.CharField(max_length=512, verbose_name=u"Вариант ответа")
    value = JSONField(verbose_name=u"Коэффициент")

    class Meta:
        verbose_name = u"Вариант ответа"
        verbose_name_plural = u"Варианты ответов"
        ordering = ['id']

    def __unicode__(self):
        return u"[{1}...] {0.text}".format(self, remove_tags(self.question.description).strip('. ')[:20])


class Student(models.Model):
    GENDER = {
        True: u"Мужской",
        False: u"Женский",
    }

    surname = models.CharField(max_length=60, verbose_name=u"фамилия", db_index=True, null=False, blank=False)
    name = models.CharField(max_length=60, verbose_name=u"имя", db_index=True, null=False, blank=False)
    middlename = models.CharField(max_length=60, verbose_name=u"отчество", db_index=True, null=False, blank=False)
    # group = models.CharField(max_length=60, verbose_name=u"группа", db_index=True, null=True, blank=True)
    age = models.PositiveSmallIntegerField(verbose_name=u"возраст", db_index=True, null=False, blank=False)
    sex = models.BooleanField(choices=GENDER.items(), db_index=True, null=False, blank=False, verbose_name=u"Пол")
    stgroup = models.ForeignKey("StudentGroup", verbose_name=u"группа", related_name='students')
    
    class Meta:
        unique_together = (
            ('surname', 'middlename', 'name', 'stgroup', 'age', 'sex'),
        )
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенты"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        self.name = self.name.strip(' ')
        self.middlename = self.middlename.strip(' ')
        self.surname = self.surname.strip(' ')
        return super(Student, self).save()

    def __unicode__(self):
        return u"{0.surname} {0.name} {0.middlename} [{0.stgroup}]".format(self)


class TestResult(models.Model):
    session = models.CharField(
        verbose_name=u"сеанс",
        null=True,
        editable=False,
        max_length=128,
        default=None
    )
    timestamp = models.DateTimeField(
        auto_created=True,
        verbose_name=u"время прохождения теста",
        editable=False,
        db_index=True,
        default=datetime.datetime.now
    )
    student = models.ForeignKey(Student, verbose_name=u"студент", db_index=True)
    test = models.ForeignKey(Test, verbose_name=u"Тест", db_index=True)
    answers = JSONField(verbose_name=u'ответы', default=[], indent=1)
    result = JSONField(verbose_name=u'результаты', indent=1)

    def __unicode__(self):
        return u"{0.timestamp} {0.student.surname} {0.student.name} {0.student.middlename}".format(self)

    def gen_result(self):
        self.result = nodeproxy.execute(
            self.test.func,
            g={
                'student': {
                    'name': self.student.name,
                    'middlename': self.student.middlename,
                    'surname': self.student.surname,
                    'age': self.student.age,
                    'sex': self.student.sex,
                }
            },
            args=[self.answers,]
        )
        self.save()

    class Meta:
        verbose_name = u"Результат тестирования"
        verbose_name_plural = u"Результаты тестирования"
