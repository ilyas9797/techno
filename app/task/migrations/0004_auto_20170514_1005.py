# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 10:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20170514_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='estimate',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 14, 10, 5, 12, 758548), validators=[task.models.datetime_validate]),
        ),
    ]