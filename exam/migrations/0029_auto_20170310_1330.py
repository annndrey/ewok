# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0028_auto_20170310_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='tests',
            field=models.ManyToManyField(related_name='teacher', verbose_name='\u0442\u0435\u0441\u0442\u044b', to='exam.Test', blank=True),
        ),
    ]
