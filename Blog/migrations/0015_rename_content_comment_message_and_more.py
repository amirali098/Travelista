# Generated by Django 4.2.11 on 2024-04-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0014_rename_posts_post_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='counted_views',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default=None, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
