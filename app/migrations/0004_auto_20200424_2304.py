# Generated by Django 3.0.4 on 2020-04-25 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200424_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='cartelera',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
