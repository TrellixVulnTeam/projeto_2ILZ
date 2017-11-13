# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('data_nascimento', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('curso', models.CharField(max_length=100)),
                ('data_nascimento', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('data_nascimento', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=10)),
                ('telefone', models.CharField(max_length=15)),
                ('celular', models.CharField(max_length=15)),
            ],
        ),
    ]
