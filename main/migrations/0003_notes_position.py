# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-10 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tb_from_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='position',
            field=models.CharField(default=None, max_length=255),
        ),
    ]