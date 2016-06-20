# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('employer', models.ForeignKey(to='jobs.Employer')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LocationMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('location', models.ForeignKey(to='jobs.Location')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('match_decimal', models.DecimalField(default=0.0, max_digits=16, decimal_places=8)),
                ('questions_answered', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user_a', models.ForeignKey(related_name='match_user_a', to=settings.AUTH_USER_MODEL)),
                ('user_b', models.ForeignKey(related_name='match_user_b', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PositionMatch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hidden', models.BooleanField(default=False)),
                ('liked', models.NullBooleanField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(to='jobs.Job')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
