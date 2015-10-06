# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0014_auto_20150930_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('name', models.CharField(max_length=140, default='', verbose_name='Name')),
                ('image', models.ImageField(verbose_name='Image', upload_to='')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date added')),
                ('updated', models.DateField(auto_now=True, verbose_name='Date updated')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['order', 'date'],
            },
        ),
    ]
