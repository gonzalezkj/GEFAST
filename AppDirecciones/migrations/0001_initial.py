# Generated by Django 4.0.1 on 2022-04-30 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id_pais', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pais',
                'verbose_name_plural': 'Paises',
            },
        ),
        migrations.CreateModel(
            name='Provincias',
            fields=[
                ('id_provincia', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('id_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppDirecciones.paises')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('id_localidad', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('codigo_postal', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('id_provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppDirecciones.provincias')),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
            },
        ),
        migrations.CreateModel(
            name='Direcciones',
            fields=[
                ('id_direccion', models.IntegerField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=40)),
                ('numero', models.PositiveIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('id_localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppDirecciones.localidades')),
            ],
            options={
                'verbose_name': 'Direccion',
                'verbose_name_plural': 'Direcciones',
            },
        ),
    ]
