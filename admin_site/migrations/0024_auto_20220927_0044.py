# Generated by Django 3.0.5 on 2022-09-26 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0023_auto_20220927_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_verify',
            field=models.IntegerField(default=0),
        ),
    ]