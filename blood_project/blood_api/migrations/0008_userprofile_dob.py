# Generated by Django 4.1.2 on 2022-10-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_api', '0007_remove_userprofile_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]
