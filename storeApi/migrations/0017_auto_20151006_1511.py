# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0016_auto_20151006_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adress',
            old_name='user',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='client',
        ),
        migrations.RenameField(
            model_name='shoppingcartproduct',
            old_name='user',
            new_name='client',
        ),
        migrations.AlterField(
            model_name='order',
            name='sku',
            field=models.SlugField(unique=True, editable=False, verbose_name='SKU'),
        ),
    ]
