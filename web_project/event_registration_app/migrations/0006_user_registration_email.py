# Generated by Django 5.0.6 on 2024-05-22 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0005_remove_user_registration_batch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
