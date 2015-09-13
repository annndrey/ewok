# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20150914_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='gender',
        ),
        migrations.AddField(
            model_name='student',
            name='sex',
            field=models.BooleanField(default=True, db_index=True, choices=[(False, '\u0416\u0435\u043d\u0441\u043a\u0438\u0439'), (True, '\u041c\u0443\u0436\u0441\u043a\u043e\u0439')]),
            preserve_default=False,
        ),
    ]
