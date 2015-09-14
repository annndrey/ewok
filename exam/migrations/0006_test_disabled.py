# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20150914_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='disabled',
            field=models.BooleanField(default=True, db_index=True, verbose_name='\u0412\u0438\u0434\u0435\u043d \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435 \u0432\u044b\u0431\u043e\u0440\u0430 \u0442\u0435\u0441\u0442\u043e\u0432'),
            preserve_default=False,
        ),
    ]
