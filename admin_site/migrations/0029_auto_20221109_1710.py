# Generated by Django 3.0.5 on 2022-11-09 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0028_auto_20221014_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='area',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(max_length=50),
        ),
    ]
