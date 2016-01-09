# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-09 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sundayfunday', '0011_auto_20160109_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('first_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person1', to=settings.AUTH_USER_MODEL)),
                ('second_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
