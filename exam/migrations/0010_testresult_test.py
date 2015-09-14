# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20150914_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(default=None, verbose_name='\u0422\u0435\u0441\u0442', to='exam.Test'),
            preserve_default=False,
        ),
    ]
