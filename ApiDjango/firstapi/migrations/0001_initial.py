# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-26 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userinfo',
            fields=[
                ('pk_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('user_name', models.CharField(max_length=80)),
            ],
        ),
    ]
