# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0021_auto_20150929_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.BooleanField(db_index=True, verbose_name='\u041f\u043e\u043b', choices=[(False, '\u0416\u0435\u043d\u0441\u043a\u0438\u0439'), (True, '\u041c\u0443\u0436\u0441\u043a\u043e\u0439')]),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 0, 54, 7, 9665), editable=False, verbose_name='\u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u0441\u0442\u0430', auto_created=True, db_index=True),
        ),
    ]
