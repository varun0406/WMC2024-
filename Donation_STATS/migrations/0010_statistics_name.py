# Generated by Django 4.2.13 on 2024-07-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_STATS', '0009_statistics_ranking'),
    ]

    operations = [
        migrations.AddField(
            model_name='statistics',
            name='Name',
            field=models.CharField(default='unknown', max_length=100),
        ),
    ]
