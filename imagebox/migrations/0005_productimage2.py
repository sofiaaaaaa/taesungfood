# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagebox', '0004_delete_제품이미지2'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d')),
            ],
        ),
    ]
