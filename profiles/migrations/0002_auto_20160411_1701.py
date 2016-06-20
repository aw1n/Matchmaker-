# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userjob',
            name='employer_name',
            field=models.CharField(max_length=220, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='location',
            field=models.CharField(max_length=220, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='position',
            field=models.CharField(max_length=220, null=True, blank=True),
        ),
    ]
