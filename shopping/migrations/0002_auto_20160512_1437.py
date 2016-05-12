# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-12 14:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'cart',
                'ordering': ['add_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_date', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'order',
                'ordering': ['deal_date'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('tags', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('obj', models.CharField(choices=[('M', 'MAN'), ('W', 'WOMAN')], max_length=20)),
                ('edit_time', models.DateTimeField(default=datetime.datetime.now)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Brands')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('level', models.IntegerField()),
                ('sub_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'product_comment',
                'ordering': ['sub_date'],
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='./static/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Product')),
            ],
            options={
                'db_table': 'product_image',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], default='M', max_length=30)),
                ('birthdate', models.DateField()),
                ('home_num', models.CharField(max_length=40)),
                ('phone_num', models.CharField(max_length=40)),
                ('addr', models.CharField(max_length=100)),
                ('addr_backup', models.CharField(max_length=100)),
                ('register_date', models.DateTimeField(default=datetime.datetime.now)),
                ('info', models.TextField()),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='addr',
        ),
        migrations.RemoveField(
            model_name='user',
            name='addr_backup',
        ),
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='home_num',
        ),
        migrations.RemoveField(
            model_name='user',
            name='info',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_num',
        ),
        migrations.AddField(
            model_name='user',
            name='pwd',
            field=models.CharField(default='88888888', max_length=50),
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.User'),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='auth',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.User'),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.User'),
        ),
        migrations.AddField(
            model_name='cart',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.User'),
        ),
    ]