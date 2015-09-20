# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storeApi', '0004_auto_20150920_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(default='', max_length=140, verbose_name='Name')),
                ('type', models.CharField(choices=[('BIL', 'Billing'), ('SHI', 'Shipping')], default='BIL', max_length=3, verbose_name='Type')),
                ('default', models.BooleanField()),
                ('firstname', models.CharField(max_length=50, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=50, verbose_name='Lastname')),
                ('adress_line1', models.CharField(max_length=140, verbose_name='Address 1')),
                ('adress_line2', models.CharField(max_length=140, verbose_name='Address 2')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state_province', models.CharField(max_length=50, verbose_name='State/Providence')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('zipcode', models.CharField(max_length=32, verbose_name='ZIP code')),
                ('phone_number', models.CharField(max_length=40, verbose_name='Phone number')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date added')),
            ],
            options={
                'verbose_name': 'adress',
                'ordering': ['default', 'date', 'name'],
                'verbose_name_plural': 'adresses',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['order', 'date', 'sku'], 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=140, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='adress',
            name='user',
            field=models.ForeignKey(to='storeApi.Client'),
        ),
    ]
