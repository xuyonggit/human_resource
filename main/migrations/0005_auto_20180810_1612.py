# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-10 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180810_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]