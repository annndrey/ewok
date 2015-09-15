# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0013_auto_20150915_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='session',
            field=models.CharField(default=None, max_length=128, null=True, editable=False, verbose_name='\u0441\u0435\u0430\u043d\u0441'),
        ),
        migrations.AddField(
            model_name='testresult',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 15, 17, 33, 58, 743853), editable=False, verbose_name='\u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u0441\u0442\u0430', auto_created=True, db_index=True),
        ),
        migrations.AlterUniqueTogether(
            name='testresult',
            unique_together=set([]),
        ),
    ]
