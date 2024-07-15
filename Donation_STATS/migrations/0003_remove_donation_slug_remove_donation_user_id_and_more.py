# Generated by Django 4.2.13 on 2024-07-13 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation_STATS', '0002_rename_donatiers_name_statistics_donaters_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='donation',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='statistics',
            name='Donaters_name',
        ),
        migrations.AddField(
            model_name='statistics',
            name='Donaters_UserID',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='statistics',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
