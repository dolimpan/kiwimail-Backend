# Generated by Django 4.2.6 on 2024-01-02 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_insta_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='insta',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
