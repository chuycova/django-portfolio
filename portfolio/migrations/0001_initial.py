# Generated by Django 3.2.6 on 2021-09-28 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(blank=True, max_length=250)),
                ('imagen', models.ImageField(upload_to='portfolio/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
