# Generated by Django 4.0.1 on 2022-05-30 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppArticulos', '0002_rename_codigo_articulo_cantidad'),
        ('AppFactura', '0004_remove_comprobantev_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleV',
            fields=[
                ('id_detalle', models.IntegerField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('monto_unitario', models.FloatField()),
                ('id_articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppArticulos.articulo')),
            ],
        ),
    ]
