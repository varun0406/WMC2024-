# Generated by Django 5.0.4 on 2024-07-29 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_userquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('testimonial_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('Name', models.CharField(max_length=100)),
                ('Occupation', models.CharField(max_length=100)),
                ('testimonial', models.TextField()),
                ('testimonial_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
