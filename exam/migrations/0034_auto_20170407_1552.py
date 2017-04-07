# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0033_auto_20170407_1551'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='stsroup',
            new_name='stgroup',
        ),
    ]
