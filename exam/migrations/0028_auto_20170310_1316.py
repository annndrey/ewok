# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0027_auto_20170310_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='stgroup',
            field=models.OneToOneField(related_name='teacher', primary_key=True, default=4, serialize=False, to='exam.StudentGroup', verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430'),
        ),
    ]
