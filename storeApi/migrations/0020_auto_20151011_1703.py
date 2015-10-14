# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0019_auto_20151006_1546'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='adress',
            options={'ordering': ['client', 'default', 'date', 'name'], 'verbose_name': 'adress', 'verbose_name_plural': 'adresses'},
        ),
    ]
