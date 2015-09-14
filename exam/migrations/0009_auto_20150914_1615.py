# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_test_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='\u041f\u043e\u0440\u044f\u0434\u043e\u043a \u0432\u043e\u043f\u0440\u043e\u0441\u0430'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='test',
            name='disabled',
            field=models.BooleanField(default=True, db_index=True, verbose_name='\u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d'),
        ),
        migrations.AlterField(
            model_name='test',
            name='timeout',
            field=models.TimeField(default=datetime.time(0, 40), verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterUniqueTogether(
            name='question',
            unique_together=set([('test', 'number')]),
        ),
    ]
