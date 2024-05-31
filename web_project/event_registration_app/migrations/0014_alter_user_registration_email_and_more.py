# Generated by Django 5.0.6 on 2024-05-22 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0013_remove_user_registration_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_registration',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('bkash', 'Bkash'), ('nagad', 'Nagad'), ('rocket', 'Rocket'), ('card', 'Card')], max_length=10),
        ),
    ]