# Generated by Django 5.0.6 on 2024-05-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_registration_app', '0043_groupeventinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='adminuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]