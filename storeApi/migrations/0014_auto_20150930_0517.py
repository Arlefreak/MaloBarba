# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0013_productimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='', blank=True, verbose_name='Main image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.SlugField(unique=True, editable=False, verbose_name='SKU'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='Date added'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='name',
            field=models.CharField(default='', max_length=140, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='updated',
            field=models.DateField(auto_now=True, verbose_name='Date updated'),
        ),
    ]
