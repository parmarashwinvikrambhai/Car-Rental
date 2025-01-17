# Generated by Django 3.0.5 on 2022-10-02 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_site', '0024_auto_20220927_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='payments',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('transfer_id', models.CharField(max_length=30)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_site.booking')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_site.users')),
            ],
        ),
    ]
