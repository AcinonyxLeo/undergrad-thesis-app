# Generated by Django 5.1.7 on 2025-03-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lora', '0002_lora_details_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lora_details',
            name='rssi',
            field=models.FloatField(null=True),
        ),
    ]
