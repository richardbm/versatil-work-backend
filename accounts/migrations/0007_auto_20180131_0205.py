# Generated by Django 2.0 on 2018-01-31 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_facebook_picture_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='token',
            name='user',
        ),
        migrations.DeleteModel(
            name='Token',
        ),
    ]
