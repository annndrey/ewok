# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0032_teacher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='stgroup',
            field=models.ManyToManyField(related_name='teachers', null=True, verbose_name=b'\xd0\x93\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd1\x8b', to='exam.StudentGroup', blank=True),
        ),
    ]
