# Generated by Django 5.0.6 on 2024-05-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0015_alter_user_registration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
