# Generated by Django 4.0.3 on 2022-04-07 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0005_alter_users_dl_image_alter_users_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dl_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
