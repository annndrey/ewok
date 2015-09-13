# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('surname', models.CharField(max_length=60, verbose_name='\u0444\u0430\u043c\u0438\u043b\u0438\u044f', db_index=True)),
                ('name', models.CharField(max_length=60, verbose_name='\u0438\u043c\u044f', db_index=True)),
                ('middlename', models.CharField(max_length=60, verbose_name='\u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e', db_index=True)),
                ('group', models.CharField(max_length=60, verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430', db_index=True)),
                ('age', models.PositiveSmallIntegerField(verbose_name='\u0432\u043e\u0437\u0440\u0430\u0441\u0442', db_index=True)),
                ('gender', models.PositiveSmallIntegerField(db_index=True, choices=[(b'male', '\u041c\u0443\u0436\u0441\u043a\u043e\u0439'), (b'female', '\u0416\u0435\u043d\u0441\u043a\u0438\u0439')])),
            ],
        ),
        migrations.AddField(
            model_name='test',
            name='timeout',
            field=models.TimeField(default=datetime.time(0,0,0), verbose_name='\u041c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0435 \u0432\u0440\u0435\u043c\u044f \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together=set([('surname', 'middlename', 'name')]),
        ),
    ]
