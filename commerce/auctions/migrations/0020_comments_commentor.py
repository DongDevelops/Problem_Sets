# Generated by Django 4.1.5 on 2023-02-16 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_rename_comments_comments_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='commentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentor', to=settings.AUTH_USER_MODEL),
        ),
    ]