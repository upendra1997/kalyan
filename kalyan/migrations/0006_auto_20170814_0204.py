# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-13 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kalyan', '0005_auto_20170814_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complains',
            name='many_category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='kalyan.Category'),
        ),
    ]
