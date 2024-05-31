# Generated by Django 5.0.6 on 2024-05-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0030_remove_registrationforpage_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationforpage',
            name='email',
            field=models.EmailField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registrationforpage',
            name='username',
            field=models.CharField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]