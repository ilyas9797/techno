# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-23 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0008_auto_20170523_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Завершено?',
        ),
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Завершено?'),
        ),
    ]