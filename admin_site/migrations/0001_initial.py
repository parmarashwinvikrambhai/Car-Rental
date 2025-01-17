# Generated by Django 4.0.3 on 2022-04-06 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('comany_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('loctoin_id', models.AutoField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'locaton',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('users_id', models.AutoField(primary_key=True, serialize=False)),
                ('dl_number', models.CharField(max_length=15)),
                ('dl_image', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('users_email', models.EmailField(max_length=100)),
                ('users_password', models.CharField(max_length=100)),
                ('users_addres', models.CharField(max_length=250)),
                ('users_phone', models.IntegerField()),
                ('is_admin', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('reg_number', models.CharField(max_length=11)),
                ('model_name', models.CharField(max_length=20)),
                ('img_car', models.ImageField(upload_to='')),
                ('model_year', models.CharField(max_length=20)),
                ('available_flag', models.IntegerField()),
                ('mileage', models.CharField(max_length=25)),
                ('fuels_type', models.CharField(max_length=20)),
                ('no_seats', models.IntegerField()),
                ('cost', models.FloatField()),
                ('car_type', models.CharField(max_length=20)),
                ('transmission', models.CharField(max_length=20)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_site.company')),
            ],
            options={
                'db_table': 'car',
            },
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_date', models.DateField()),
                ('return_date', models.DateField()),
                ('booking_status', models.IntegerField()),
                ('amount', models.FloatField()),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_site.car')),
                ('drop_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='drop_location', to='admin_site.location')),
                ('pickup_location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pickup_location', to='admin_site.location')),
                ('users_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='admin_site.users')),
            ],
            options={
                'db_table': 'booking',
            },
        ),
    ]
