# Generated by Django 2.0.5 on 2018-06-07 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alumno'),
    ]

    operations = [
        migrations.CreateModel(
            name='datos',
            fields=[
                ('idMateria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('descripcion', models.CharField(max_length=130)),
            ],
        ),
    ]
