# Generated by Django 3.2 on 2021-07-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarjetas', '0007_alter_tarjeta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarjeta',
            name='numero',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
