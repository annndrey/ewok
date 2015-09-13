# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20150913_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(verbose_name='\u0432\u043e\u0437\u0440\u0430\u0441\u0442', db_index=True),
        ),
    ]
