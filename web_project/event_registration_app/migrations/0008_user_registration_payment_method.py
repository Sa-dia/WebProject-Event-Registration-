# Generated by Django 5.0.6 on 2024-05-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0007_user_registration_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('bkash', 'Bkash'), ('nagad', 'Nagad'), ('rocket', 'Rocket'), ('card', 'Card')], default=0, max_length=10),
            preserve_default=False,
        ),
    ]
