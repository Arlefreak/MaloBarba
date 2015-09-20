# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.SlugField(unique=True, verbose_name='SKU')),
                ('name', models.CharField(max_length=140, default=' ', verbose_name='Name')),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Main image')),
                ('price', models.FloatField(default=0.0, verbose_name='Price')),
                ('discount', models.FloatField(default=0.0, verbose_name='Discount')),
                ('inventory', models.IntegerField(default=0, verbose_name='Inventory')),
                ('status', models.CharField(max_length=3, default='OUT', choices=[('IN', 'In stock'), ('OUT', 'Out of stock')], verbose_name='Status')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', through='taggit.TaggedItem', help_text='A comma-separated list of tags.')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
