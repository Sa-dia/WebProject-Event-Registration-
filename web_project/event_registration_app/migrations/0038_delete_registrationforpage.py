# Generated by Django 5.0.6 on 2024-05-24 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0037_alter_registrationforpage_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegistrationForPage',
        ),
    ]
