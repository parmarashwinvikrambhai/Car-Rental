# Generated by Django 4.0.3 on 2022-04-06 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img_car',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='dl_image',
            field=models.CharField(max_length=20),
        ),
    ]
