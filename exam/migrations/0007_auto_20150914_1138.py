# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_test_disabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='disabled',
            field=models.BooleanField(db_index=True, verbose_name='\u041e\u0442\u043a\u043b\u044e\u0447\u0435\u043d'),
        ),
    ]
