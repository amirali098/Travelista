# Generated by Django 4.2.11 on 2024-04-17 20:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 20, 46, 17, 102699, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='posts',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 17, 20, 46, 17, 102699, tzinfo=datetime.timezone.utc)),
        ),
    ]
