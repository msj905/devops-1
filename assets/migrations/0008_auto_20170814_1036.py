# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-14 02:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20170814_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(3, '故障'), (2, '已下线'), (1, '在线'), (4, '备用')], default=1, null=True, verbose_name='资产状态'),
        ),
        migrations.AlterField(
            model_name='networkdevice',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(3, '故障'), (2, '已下线'), (1, '在线'), (4, '备用')], default=1, verbose_name='资产状态'),
        ),
    ]
