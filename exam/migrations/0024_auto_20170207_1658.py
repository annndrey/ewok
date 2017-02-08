# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0023_auto_20151002_0109'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('description', redactor.fields.RedactorField(default=b'', verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True)),
            ],
            options={
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b',
            },
        ),
        migrations.AlterField(
            model_name='test',
            name='func',
            field=models.TextField(default=b'function (answers) {\n    // this.student.sex\n    // this.student.age\n    var result = {};\n    answers.map(function (answer, number) {\n        result[number+1] = answer.answer;\n    });\n    return result;\n}'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False, verbose_name='\u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u0441\u0442\u0430', auto_created=True, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('surname', 'middlename', 'name', 'stgroup', 'age', 'sex')]),
        ),
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.AddField(
            model_name='student',
            name='stgroup',
            field=models.ForeignKey(related_name='students', default=1, verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430', to='exam.StudentGroup'),
            preserve_default=False,
        ),
    ]
