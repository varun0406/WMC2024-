# Generated by Django 5.0.4 on 2024-07-28 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_karmapoints_reference_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserQuery',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=254)),
                ('query', models.TextField()),
                ('query_date', models.DateTimeField(auto_now_add=True)),
                ('query_status', models.CharField(default='Pending', max_length=100)),
            ],
        ),
    ]
