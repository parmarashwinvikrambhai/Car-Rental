# Generated by Django 4.0.3 on 2022-04-10 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0011_rename_comany_name_company_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img_car',
            field=models.CharField(max_length=200),
        ),
    ]