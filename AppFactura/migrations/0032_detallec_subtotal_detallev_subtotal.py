# Generated by Django 4.0.1 on 2022-07-15 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFactura', '0031_remove_comprobantev_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallec',
            name='subtotal',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detallev',
            name='subtotal',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]