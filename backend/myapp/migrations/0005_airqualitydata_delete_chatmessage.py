# Generated by Django 5.1.7 on 2025-04-16 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_chatsession_rename_bot_response_chatmessage_bot_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirQualityData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('co2', models.FloatField(verbose_name='Carbon dioxide (CO2)')),
                ('no2', models.FloatField(verbose_name='Nitrogen dioxide (NO2)')),
                ('nh4', models.FloatField(verbose_name='Ammonia (NH4)')),
                ('c6h6', models.FloatField(verbose_name='Benzene (C6H6)')),
                ('co', models.FloatField(verbose_name='Carbon Monoxide (CO)')),
                ('time_minutes', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]
