# Generated by Django 4.0.3 on 2022-04-12 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0012_alter_car_img_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='loction_id',
            new_name='location_id',
        ),
        migrations.AlterModelTable(
            name='location',
            table='location',
        ),
    ]