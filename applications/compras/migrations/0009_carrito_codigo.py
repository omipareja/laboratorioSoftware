# Generated by Django 3.2 on 2021-05-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0008_remove_carrito_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='codigo',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
