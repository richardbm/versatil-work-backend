# Generated by Django 2.0 on 2018-01-24 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0007_auto_20171228_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseToActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('price', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='activity.Activity')),
                ('owner', models.ForeignKey(on_delete=models.SET(1), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
