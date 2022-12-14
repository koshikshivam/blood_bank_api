# Generated by Django 4.1.2 on 2022-10-27 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blood_api', '0002_remove_blood_donation_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blood_donation',
            name='blood_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_api.category'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='blood_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_api.category'),
        ),
    ]
