# Generated by Django 4.1.5 on 2023-02-13 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listings_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listings',
            name='image_url',
        ),
    ]