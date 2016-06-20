# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='location',
            name='pub_date',
        ),
    ]
