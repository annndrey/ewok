# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0026_auto_20170228_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='id',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='stgroup',
            field=models.OneToOneField(related_name='teacher', primary_key=True, serialize=False, to='exam.StudentGroup', verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430'),
        ),
    ]
