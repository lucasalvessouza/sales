# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-04 13:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20180303_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='excluded',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='excluded_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='cellphone',
            field=models.CharField(blank=True, max_length=17, verbose_name='Telefone'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 4, 13, 59, 6, 388029)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 4, 13, 59, 6, 387984)),
        ),
    ]