# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-03 18:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20180303_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 3, 18, 55, 51, 943432)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 3, 18, 55, 51, 943387)),
        ),
    ]
