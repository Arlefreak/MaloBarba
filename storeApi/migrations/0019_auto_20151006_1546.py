# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0018_auto_20151006_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(editable=False, default='PRO', verbose_name='status', choices=[('PRO', 'processing'), ('SHI', 'shipped'), ('COM', 'complete')], max_length=3),
        ),
    ]
