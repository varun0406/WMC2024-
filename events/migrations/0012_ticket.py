# Generated by Django 5.0.4 on 2024-08-01 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_delete_ticket'),
        ('login', '0010_testimonial_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.SmallIntegerField()),
                ('total_paid_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('attendee_name', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('discount', models.IntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.profile')),
            ],
        ),
    ]
