# Generated by Django 2.0 on 2017-12-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='category',
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='activity.Category'),
            preserve_default=False,
        ),
    ]
