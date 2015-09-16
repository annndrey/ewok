# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0018_auto_20150917_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='answers',
            field=jsonfield.fields.JSONField(default=[], verbose_name='\u043e\u0442\u0432\u0435\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 1, 3, 19, 463564), editable=False, verbose_name='\u0432\u0440\u0435\u043c\u044f \u043f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u044f \u0442\u0435\u0441\u0442\u0430', auto_created=True, db_index=True),
        ),
    ]
