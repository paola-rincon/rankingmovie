# Generated by Django 3.0.4 on 2020-04-25 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200424_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='categoria',
        ),
        migrations.AddField(
            model_name='categoria',
            name='peliculas',
            field=models.ManyToManyField(to='app.Pelicula'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='actores',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
