# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_auto_20160512_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
