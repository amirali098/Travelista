# Generated by Django 4.2.11 on 2024-04-17 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_posts_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='counted_views',
            field=models.IntegerField(default=0),
        ),
    ]
