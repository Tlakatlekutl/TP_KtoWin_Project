# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-13 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ktoWin', '0007_like_like_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='like_status',
            field=models.IntegerField(choices=[(1, 1), (-1, -1)], default=1),
        ),
    ]
