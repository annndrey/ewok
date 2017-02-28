# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0025_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': '\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u044c', 'verbose_name_plural': '\u041f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0438'},
        ),
        migrations.AddField(
            model_name='teacher',
            name='tests',
            field=models.ManyToManyField(related_name='teacher', null=True, verbose_name='\u0442\u0435\u0441\u0442\u044b', to='exam.Test'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='stgroup',
            field=models.ForeignKey(related_name='teacher', verbose_name='\u0433\u0440\u0443\u043f\u043f\u0430', to='exam.StudentGroup', null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(verbose_name='\u0443\u0447\u0435\u0442\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c', to=settings.AUTH_USER_MODEL),
        ),
    ]
