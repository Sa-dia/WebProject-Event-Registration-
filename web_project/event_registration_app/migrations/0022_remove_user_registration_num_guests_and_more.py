# Generated by Django 5.0.6 on 2024-05-23 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0021_alter_user_registration_num_guests'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_registration',
            name='num_guests',
        ),
        migrations.AddField(
            model_name='user_registration',
            name='guests',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
