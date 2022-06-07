# Generated by Django 4.0.1 on 2022-05-30 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFactura', '0005_detallev'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detallev',
            old_name='id_articulo',
            new_name='id_art',
        ),
        migrations.RemoveField(
            model_name='detallev',
            name='id_detalle',
        ),
        migrations.AddField(
            model_name='detallev',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detallev',
            name='cantidad',
            field=models.IntegerField(default=1),
        ),
    ]
