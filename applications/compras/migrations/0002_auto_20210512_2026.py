# Generated by Django 3.1.7 on 2021-05-12 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallecompra',
            name='compras',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='compras.compras'),
        ),
    ]
