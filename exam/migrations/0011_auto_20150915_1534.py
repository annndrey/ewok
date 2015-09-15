# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_testresult_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testresult',
            name='answers',
            field=jsonfield.fields.JSONField(default=[], verbose_name='\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b'),
        ),
        migrations.AlterUniqueTogether(
            name='testresult',
            unique_together=set([('student', 'test')]),
        ),
    ]
