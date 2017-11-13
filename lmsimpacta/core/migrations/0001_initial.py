# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 03:41
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome', models.CharField(max_length=50)),
                ('ra', models.IntegerField(unique=True)),
                ('password', models.CharField(max_length=150)),
                ('perfil', models.CharField(default='C', max_length=1)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', core.models.UsuarioManager()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=5)),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(blank=True, max_length=50)),
                ('carga_horaria', models.IntegerField(default=1000)),
                ('ativo', models.BooleanField(default=True)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
    ]
