# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0031_auto_20170314_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variant',
            options={'ordering': ['id'], 'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430', 'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u043e\u0432'},
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.PositiveSmallIntegerField(db_index=True, verbose_name='\u0422\u0438\u043f', choices=[(0, '\u041e\u0434\u0438\u043d \u0438\u0437 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u043e\u0442\u0432\u0435\u0442\u0430, \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e'), (1, '\u041d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u043e\u0442\u0432\u0435\u0442\u0430'), (2, '\u041e\u0442\u0432\u0435\u0442 \u0432 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e\u0439 \u0444\u043e\u0440\u043c\u0435'), (3, '\u041e\u0434\u0438\u043d \u0438\u0437 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u043e\u0442\u0432\u0435\u0442\u0430, \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e')]),
        ),
    ]
