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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=10, choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D'), ('e', 'E'), ('f', 'F'), ('g', 'G'), ('h', 'H'), ('i', 'I'), ('j', 'J')])),
                ('date', models.DateTimeField()),
                ('premium_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('premium_currency', models.CharField(max_length=3, choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')])),
                ('limit_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('limit_currency', models.CharField(max_length=3, choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')])),
                ('franchise_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('franchise_currency', models.CharField(max_length=3, choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')])),
                ('attachment_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('attachment_currency', models.CharField(max_length=3, choices=[('usd', 'US Dollars'), ('cad', 'Canadian Dollars')])),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('contracts', models.ManyToManyField(to='contracts.Contract')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='authors',
            field=models.ManyToManyField(to='contracts.Person'),
        ),
    ]
