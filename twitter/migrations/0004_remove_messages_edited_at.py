# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-10 20:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_messages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='edited_at',
        ),
    ]