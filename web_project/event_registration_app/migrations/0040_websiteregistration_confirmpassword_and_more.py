# Generated by Django 5.0.6 on 2024-05-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0039_websiteregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteregistration',
            name='confirmpassword',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='websiteregistration',
            name='password',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
