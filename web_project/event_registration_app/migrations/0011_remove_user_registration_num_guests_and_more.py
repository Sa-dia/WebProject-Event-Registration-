# Generated by Django 5.0.6 on 2024-05-22 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0010_remove_user_registration_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration',
            name='num_guests',
        ),
        migrations.RemoveField(
            model_name='user_registration',
            name='total_payment',
        ),
    ]
