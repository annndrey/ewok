# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_auto_20150914_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='priority',
            field=models.IntegerField(default=1000, verbose_name='\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0438', db_index=True),
        ),
    ]
