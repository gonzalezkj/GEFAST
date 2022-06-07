# Generated by Django 4.0.1 on 2022-05-30 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppFactura', '0002_puntosdeventa_alter_tipocomprobante_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobanteV',
            fields=[
                ('id_comprobante', models.IntegerField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
                ('fecha', models.DateField()),
                ('total', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('id_punto_de_venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFactura.puntosdeventa')),
                ('id_tipo_comprobante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppFactura.tipocomprobante')),
            ],
            options={
                'verbose_name': 'ComprobanteV',
                'verbose_name_plural': 'ComprobantesV',
            },
        ),
    ]