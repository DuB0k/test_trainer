# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='test_name',
            new_name='test_text',
        ),
    ]
