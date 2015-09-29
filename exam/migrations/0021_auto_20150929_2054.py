# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0020_auto_20150918_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='func',
            field=models.TextField(default=b'function (answers) {\n    // global.student.sex\n    // global.student.age\n    var result = [];\n    answers.map(function (answer) {\n        result.push(answer);\n    });\n    return result;\n}'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 29, 20, 54, 29, 408574), editable=False, verbose_name='\u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u0441\u0442\u0430', auto_created=True, db_index=True),
        ),
    ]
