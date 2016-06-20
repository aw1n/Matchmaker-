# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=120, null=True, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=profiles.models.upload_location, blank=True)),
                ('Description', models.TextField()),
                ('CV', models.FileField(upload_to=profiles.models.upload_location)),
                ('skills', models.CharField(max_length=200, null=True, blank=True)),
                ('project', models.FileField(upload_to=profiles.models.upload_location)),
                ('projecturl', models.URLField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=220)),
                ('location', models.CharField(max_length=220)),
                ('employer_name', models.CharField(max_length=220)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
