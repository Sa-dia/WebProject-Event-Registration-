# Generated by Django 5.0.6 on 2024-05-22 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0003_rename_user_user_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='num_guests',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3')], max_length=50),
        ),
    ]
