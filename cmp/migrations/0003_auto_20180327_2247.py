# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-27 22:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmp', '0002_auto_20180327_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(help_text='Укажите должность сотрудника', on_delete=django.db.models.deletion.CASCADE, to='cmp.Job', verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='knowledge',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='proficiency',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Название'),
        ),
    ]
