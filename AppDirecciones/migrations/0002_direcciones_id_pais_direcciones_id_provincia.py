# Generated by Django 4.0.1 on 2022-06-24 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppDirecciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='direcciones',
            name='id_pais',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppDirecciones.paises'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='direcciones',
            name='id_provincia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AppDirecciones.provincias'),
            preserve_default=False,
        ),
    ]
