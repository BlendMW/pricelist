# Generated by Django 5.0.9 on 2024-11-03 22:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Destination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travel_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('airline', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('commission', models.FloatField()),
                ('currency', models.CharField(choices=[('IQD', 'Iraqi Dinar'), ('USD', 'US Dollar')], max_length=3)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=15)),
                ('seats_remaining', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Destination.destination')),
            ],
        ),
    ]
