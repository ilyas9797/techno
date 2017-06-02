# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_auto_20170514_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='estimate',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[task.models.datetime_validate]),
        ),
    ]