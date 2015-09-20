# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeApi', '0005_auto_20150920_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sku', models.SlugField(verbose_name='SKU', unique=True)),
                ('items_subTotal', models.FloatField(verbose_name='Items subtotal')),
                ('shipping_cost', models.FloatField(verbose_name='Shipping cost')),
                ('taxes_cost', models.FloatField(verbose_name='Taxes costs')),
                ('total', models.FloatField(verbose_name='Total')),
                ('shipping_carrier', models.CharField(verbose_name='Shipping carrier', max_length=50)),
                ('shipping_tracking', models.CharField(verbose_name='Shipping tracking numer', max_length=50)),
                ('date', models.DateField(verbose_name='Date placed', auto_now_add=True)),
                ('updated', models.DateField(verbose_name='Date updated', auto_now=True)),
                ('status', models.CharField(verbose_name='status', choices=[('PRO', 'processing'), ('SHI', 'shipped'), ('COM', 'complete')], max_length=3, default='PRO')),
            ],
            options={
                'verbose_name_plural': 'orders',
                'verbose_name': 'order',
                'ordering': ['date', 'sku'],
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cuantity', models.IntegerField()),
                ('order', models.ForeignKey(to='storeApi.Order')),
                ('product', models.ForeignKey(to='storeApi.Product')),
            ],
            options={
                'verbose_name_plural': 'order products',
                'verbose_name': 'order product',
                'ordering': ['cuantity'],
            },
        ),
        migrations.CreateModel(
            name='ShoppingCartProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('cuantity', models.IntegerField()),
                ('product', models.ForeignKey(to='storeApi.Product')),
            ],
            options={
                'verbose_name_plural': 'shopping cart products',
                'verbose_name': 'shopping cart product',
                'ordering': ['cuantity'],
            },
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'clients', 'verbose_name': 'client', 'ordering': ['user']},
        ),
        migrations.AlterField(
            model_name='adress',
            name='adress_line2',
            field=models.CharField(verbose_name='Address 2', blank=True, max_length=140),
        ),
        migrations.DeleteModel(
            name='ShoppingCart',
        ),
        migrations.AddField(
            model_name='shoppingcartproduct',
            name='user',
            field=models.ForeignKey(to='storeApi.Client'),
        ),
        migrations.AddField(
            model_name='order',
            name='billingAdress',
            field=models.ForeignKey(related_name='billingAdress', to='storeApi.Adress'),
        ),
        migrations.AddField(
            model_name='order',
            name='shippingAdress',
            field=models.ForeignKey(related_name='shippingAdress', to='storeApi.Adress'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(to='storeApi.Client'),
        ),
    ]
