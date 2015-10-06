# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0015_auto_20151006_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(to='storeApi.Category', default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, verbose_name='Image', upload_to='', null=True),
        ),
    ]
