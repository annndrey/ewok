# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0032_auto_20170407_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='stgroup',
            new_name='stsroup',
        ),
    ]
