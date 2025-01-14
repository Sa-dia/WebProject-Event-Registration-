# Generated by Django 5.0.6 on 2024-05-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0006_user_registration_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], default=0, max_length=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='fullname',
            field=models.CharField(max_length=255),
        ),
    ]
