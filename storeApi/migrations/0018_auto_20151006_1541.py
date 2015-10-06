# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0017_auto_20151006_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items_subTotal',
            field=models.FloatField(verbose_name='Items subtotal', default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_cost',
            field=models.FloatField(verbose_name='Shipping cost', default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='taxes_cost',
            field=models.FloatField(verbose_name='Taxes costs', default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.FloatField(verbose_name='Total', default=0),
        ),
    ]
