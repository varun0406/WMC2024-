# Generated by Django 4.2.13 on 2024-07-09 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_profile_membership_license_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.URLField(default='/img'),
        ),
    ]
