# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0007_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=b'', upload_to=b'', verbose_name=b'Main image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.SlugField(verbose_name=b'SKU', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
