# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0012_auto_20150915_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='answers',
            field=jsonfield.fields.JSONField(default=[], verbose_name='\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='result',
            field=jsonfield.fields.JSONField(default=dict, verbose_name='\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='student',
            field=models.ForeignKey(verbose_name='\u0441\u0442\u0443\u0434\u0435\u043d\u0442', to='exam.Student'),
        ),
        migrations.AlterField(
            model_name='testresult',
            name='test',
            field=models.ForeignKey(verbose_name='\u0422\u0435\u0441\u0442', to='exam.Test'),
        ),
    ]
