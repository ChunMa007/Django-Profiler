# Generated by Django 5.1.7 on 2025-03-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilerapp', '0002_rename_user_records_user_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_record',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
