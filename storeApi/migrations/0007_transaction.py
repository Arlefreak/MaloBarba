# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0006_auto_20150920_0428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('card', models.CharField(verbose_name='Token', max_length=50)),
                ('order', models.ForeignKey(to='storeApi.Order')),
            ],
        ),
    ]
