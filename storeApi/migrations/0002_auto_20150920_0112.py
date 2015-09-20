# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(verbose_name='Date added', default=datetime.datetime(2015, 9, 20, 1, 12, 36, 341520, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateField(verbose_name='Date updated', auto_now=True, default=datetime.datetime(2015, 9, 20, 1, 12, 42, 141587, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
