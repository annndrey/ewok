# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0035_auto_20170407_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='teacher',
            field=models.ForeignKey(default=1, blank=True, to='exam.Teacher', null=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xbf\xd0\xbe\xd0\xb4\xd0\xb0\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
        ),
    ]
