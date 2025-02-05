# Generated by Django 5.0.6 on 2024-05-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0041_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(blank=True, max_length=15)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3, null=True)),
                ('payment_method', models.CharField(choices=[('cash', 'Cash'), ('bkash', 'Bkash'), ('nagad', 'Nagad'), ('rocket', 'Rocket'), ('card', 'Card')], max_length=10)),
            ],
        ),
    ]
