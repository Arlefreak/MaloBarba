# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0003_remove_product_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['order', 'date', 'sku'], 'verbose_name': 'Product'},
        ),
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 1, 25, 35, 217056, tzinfo=utc), auto_now=True, verbose_name='Date updated'),
            preserve_default=False,
        ),
    ]
