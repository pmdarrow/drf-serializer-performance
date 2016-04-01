# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('premium_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('premium_currency', models.CharField(choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')], max_length=3)),
                ('limit_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('limit_currency', models.CharField(choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')], max_length=3)),
                ('franchise_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('franchise_currency', models.CharField(choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')], max_length=3)),
                ('attachment_value', models.DecimalField(max_digits=10, decimal_places=2)),
                ('attachment_currency', models.CharField(choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contracts', models.ManyToManyField(to='contracts.Contract')),
            ],
        ),
    ]
