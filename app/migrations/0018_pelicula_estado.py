# Generated by Django 3.0.4 on 2020-04-30 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200430_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='estado',
            field=models.TextField(null=True),
        ),
    ]
