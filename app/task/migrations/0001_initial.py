# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import task.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('estimate', models.DateTimeField(default=django.utils.timezone.now, validators=[task.models.datetime_validate])),
                ('creating_time', models.DateTimeField(auto_now=True)),
                ('state', models.IntegerField(choices=[(1, 'ready'), (0, 'in_progress')], default=0, verbose_name='Состояние задачи: ')),
            ],
        ),
    ]
