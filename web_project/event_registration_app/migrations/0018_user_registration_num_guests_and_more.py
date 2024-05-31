# Generated by Django 5.0.6 on 2024-05-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0017_user_registration_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='num_guests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]