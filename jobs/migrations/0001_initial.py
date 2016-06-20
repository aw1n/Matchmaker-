# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(default=b'', verbose_name=b'published')),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(unique=True, max_length=120)),
                ('slug', models.SlugField()),
                ('active', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(default=b'', verbose_name=b'published')),
                ('flagged', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=250)),
                ('slug', models.SlugField()),
                ('active', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(default=b'', verbose_name=b'published')),
                ('flagged', models.ManyToManyField(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='employer',
            name='location',
            field=models.ForeignKey(blank=True, to='jobs.Location', null=True),
        ),
    ]
