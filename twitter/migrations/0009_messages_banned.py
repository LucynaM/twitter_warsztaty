# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-13 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0008_auto_20180313_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]
