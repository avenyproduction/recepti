# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Recepti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recepti', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Trava',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trava', models.CharField(max_length=256)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepti_app.Problem')),
                ('rec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepti_app.Recepti')),
            ],
        ),
        migrations.AddField(
            model_name='recepti',
            name='probl',
            field=models.ManyToManyField(through='recepti_app.Trava', to='recepti_app.Problem'),
        ),
    ]
