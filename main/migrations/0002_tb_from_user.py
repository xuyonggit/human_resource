# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-09 07:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_from_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default=None, max_length=255, verbose_name='用户名')),
                ('recommend_count', models.IntegerField(default=0, verbose_name='已推荐人数')),
                ('reputation', models.IntegerField(default=100, verbose_name='信誉分数')),
            ],
        ),
    ]
