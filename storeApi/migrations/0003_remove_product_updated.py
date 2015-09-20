# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0002_auto_20150920_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
    ]
