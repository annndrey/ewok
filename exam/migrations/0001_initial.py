# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', redactor.fields.RedactorField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('type', models.PositiveSmallIntegerField(db_index=True, verbose_name='\u0422\u0438\u043f', choices=[(0, '\u041e\u0434\u0438\u043d \u0438\u0437 \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u043e\u0442\u0432\u0435\u0442\u0430'), (1, '\u041d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u043e\u0432 \u043e\u0442\u0432\u0435\u0442\u0430'), (2, '\u041e\u0442\u0432\u0435\u0442 \u0432 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u043e\u0439 \u0444\u043e\u0440\u043c\u0435')])),
            ],
            options={
                'verbose_name': '\u0412\u043e\u043f\u0440\u043e\u0441',
                'verbose_name_plural': '\u0412\u043e\u043f\u0440\u043e\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('func', models.TextField(default=b'function (answers) {\n    var result = [];\n    answers.map(function (answer) {\n        result.push(answer);\n    });\n    return result;\n}')),
            ],
            options={
                'verbose_name': '\u0422\u0435\u0441\u0442',
                'verbose_name_plural': '\u0422\u0435\u0441\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=512, verbose_name='\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430')),
                ('value', jsonfield.fields.JSONField(default=dict, verbose_name='\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442')),
                ('question', models.ForeignKey(to='exam.Question')),
            ],
            options={
                'verbose_name': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442 \u043e\u0442\u0432\u0435\u0442\u0430',
                'verbose_name_plural': '\u0412\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043e\u0442\u0432\u0435\u0442\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='test',
            field=models.ForeignKey(to='exam.Test'),
        ),
    ]
