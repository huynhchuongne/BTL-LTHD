# Generated by Django 4.2.13 on 2024-05-29 09:56

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DRLapp', '0003_point_confirm_user_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]