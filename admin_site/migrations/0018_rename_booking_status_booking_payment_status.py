# Generated by Django 4.0.3 on 2022-04-18 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0017_feedbacks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_status',
            new_name='payment_status',
        ),
    ]
