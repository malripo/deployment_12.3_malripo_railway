# Generated by Django 5.1.3 on 2025-01-31 21:13

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=85, scale=None, size=[600, 600], upload_to='avatars/'),
        ),
    ]
