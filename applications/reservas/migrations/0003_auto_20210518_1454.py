# Generated by Django 3.1.7 on 2021-05-18 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0002_reservas_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='estado',
            field=models.CharField(blank=True, choices=[('reservado', 'reservado'), ('cancelado', 'cancelado')], default='reservado', max_length=11, null=True),
        ),
    ]
