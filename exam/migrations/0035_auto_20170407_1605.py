# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0034_auto_20170407_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='stgroup',
        ),
        migrations.AddField(
            model_name='teacher',
            name='stgroup',
            field=models.ManyToManyField(default=4, related_name='teacher', verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430', to='exam.StudentGroup'),
        ),
    ]
