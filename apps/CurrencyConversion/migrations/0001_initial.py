# Generated by Django 5.0.9 on 2024-11-03 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversion_rate', models.FloatField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
