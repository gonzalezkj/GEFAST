# Generated by Django 4.0.1 on 2022-04-30 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppArticulos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='codigo',
            new_name='cantidad',
        ),
    ]
