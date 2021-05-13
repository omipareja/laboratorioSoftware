# Generated by Django 3.1.7 on 2021-05-10 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.TextField(unique=True)),
                ('autor', models.TextField(max_length=30)),
                ('numero_paginas', models.IntegerField()),
                ('editorial', models.TextField(max_length=50)),
                ('Fecha_publicacion', models.DateField()),
                ('idioma', models.TextField()),
                ('estado', models.CharField(choices=[('nuevo', 'nuevo'), ('usado', 'usado')], default='nuevo', max_length=15)),
                ('precio', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('categoria', models.ManyToManyField(to='libros.Category')),
            ],
        ),
    ]
