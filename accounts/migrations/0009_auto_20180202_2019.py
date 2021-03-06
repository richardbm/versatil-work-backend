# Generated by Django 2.0 on 2018-02-02 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0010_auto_20180202_1948'),
        ('accounts', '0008_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingDemand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='RatingSupply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.Activity')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='rating_demand',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rating_supply',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='ratingsupply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_rating_supply', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ratingdemand',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list_rating_demand', to=settings.AUTH_USER_MODEL),
        ),
    ]
