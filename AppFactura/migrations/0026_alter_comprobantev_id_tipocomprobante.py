# Generated by Django 4.0.1 on 2022-06-02 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFactura', '0025_detallev_porcentaje_iva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobantev',
            name='id_tipocomprobante',
            field=models.IntegerField(),
        ),
    ]
