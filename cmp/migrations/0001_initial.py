# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-24 21:11
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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('department', models.CharField(blank=True, max_length=30)),
                ('date_applyied', models.DateField(blank=True, null=True)),
                ('date_retired', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('discription', models.TextField(blank=True, max_length=500)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Knowledge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_zun', models.TextField(blank=True, max_length=500)),
                ('discription', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Proficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_zun', models.TextField(blank=True, max_length=500)),
                ('discription', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_zun', models.TextField(blank=True, max_length=500)),
                ('discription', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='knowledge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.Knowledge'),
        ),
        migrations.AddField(
            model_name='job',
            name='proficiency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.Proficiency'),
        ),
        migrations.AddField(
            model_name='job',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.Skills'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.Job'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
