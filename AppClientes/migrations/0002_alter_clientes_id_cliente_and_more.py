# Generated by Django 4.0.1 on 2022-06-02 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppClientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='id_cliente',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Nro de ID'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='razon_nombre',
            field=models.CharField(max_length=50, verbose_name='Razon o nombre'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='condicionfiscal',
            name='condicion_fiscal',
            field=models.CharField(max_length=50, verbose_name='Condicion'),
        ),
    ]
