# Generated by Django 4.0.3 on 2022-04-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0004_users_otp_users_otp_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dl_image',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='users',
            name='otp',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
    ]