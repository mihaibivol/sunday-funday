# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sundayfunday', '0010_auto_20160109_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
