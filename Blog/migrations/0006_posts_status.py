# Generated by Django 4.2.11 on 2024-04-17 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_alter_posts_published_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
