# Generated by Django 2.0 on 2018-02-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20180202_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rating_demand',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating_supply',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
