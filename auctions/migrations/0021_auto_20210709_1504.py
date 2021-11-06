# Generated by Django 3.1.1 on 2021-07-09 12:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_auto_20201222_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='time',
            field=models.CharField(default=datetime.datetime(2021, 7, 9, 12, 4, 8, 219423, tzinfo=utc), max_length=64),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.CharField(default=datetime.datetime(2021, 7, 9, 12, 4, 8, 219423, tzinfo=utc), max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
