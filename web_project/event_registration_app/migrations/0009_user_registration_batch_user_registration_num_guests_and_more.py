# Generated by Django 5.0.6 on 2024-05-22 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0008_user_registration_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='batch',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_registration',
            name='num_guests',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='trxid',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='fullname',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='payment_method',
            field=models.CharField(choices=[('cash', 'Cash'), ('bkash', 'Bkash'), ('nagad', 'Nagad'), ('rocket', 'Rocket'), ('card', 'Card')], max_length=20),
        ),
    ]
