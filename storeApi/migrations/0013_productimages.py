# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0012_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=140, verbose_name=b'Name')),
                ('image', models.ImageField(upload_to=b'', verbose_name=b'Image')),
                ('order', models.IntegerField(default=0, verbose_name=b'Order')),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Date added')),
                ('updated', models.DateField(auto_now=True, verbose_name=b'Date updated')),
                ('product', models.ForeignKey(to='storeApi.Product')),
            ],
            options={
                'ordering': ['order', 'date'],
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
    ]
