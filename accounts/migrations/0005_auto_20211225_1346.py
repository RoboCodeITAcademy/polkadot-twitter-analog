# Generated by Django 3.2.6 on 2021-12-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_title'),
        ('accounts', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='likes',
        ),
        migrations.AddField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to='main.Post'),
        ),
    ]
