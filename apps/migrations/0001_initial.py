# Generated by Django 4.1.2 on 2022-10-24 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('texto_apertura', models.TextField()),
                ('director', models.CharField(max_length=100)),
                ('productor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='planeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='personaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('altura', models.IntegerField()),
                ('masa', models.IntegerField()),
                ('color_pelo', models.CharField(max_length=50)),
                ('color_piel', models.CharField(max_length=50)),
                ('color_ojos', models.CharField(max_length=50)),
                ('año_nacimiento', models.IntegerField()),
                ('género', models.CharField(max_length=50)),
                ('mundo_natal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.planeta', verbose_name='mundo_natal')),
                ('peliculas_participa', models.ManyToManyField(to='apps.pelicula', verbose_name='peliculas')),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='planetas',
            field=models.ManyToManyField(to='apps.planeta'),
        ),
    ]
