# Generated by Django 2.0 on 2017-12-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_auto_20171228_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='background_color',
            field=models.CharField(default='rgba(255, 2290, 93, 0.5)', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='icon_color',
            field=models.CharField(default='#e4c25a', max_length=50),
            preserve_default=False,
        ),
    ]