# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-06 15:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('due', models.DateTimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('assigned_on', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.BooleanField(default=True)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_actions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
