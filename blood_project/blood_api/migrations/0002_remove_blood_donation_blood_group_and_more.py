# Generated by Django 4.1.2 on 2022-10-27 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blood_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood_donation',
            name='blood_group',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='blood_group',
        ),
    ]
