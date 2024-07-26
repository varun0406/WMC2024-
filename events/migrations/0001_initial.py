# Generated by Django 5.0.4 on 2024-07-24 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=255)),
                ('org_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('org_email', models.EmailField(blank=True, max_length=255, null=True)),
                ('org_desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_name', models.CharField(max_length=255)),
                ('venue_address', models.TextField(blank=True, null=True)),
                ('venue_contact', models.CharField(blank=True, max_length=255, null=True)),
                ('venue_capacity', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('event_desc', models.TextField(blank=True, null=True)),
                ('event_s_time', models.DateTimeField()),
                ('event_e_time', models.DateTimeField()),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.organization')),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.venue')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('attendee_name', models.CharField(blank=True, max_length=255, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
