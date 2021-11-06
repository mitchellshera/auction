# Generated by Django 3.0.8 on 2020-12-20 10:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20201220_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bids',
            name='bidowner',
        ),
        migrations.RemoveField(
            model_name='bids',
            name='bidstart',
        ),
        migrations.AlterField(
            model_name='auctionlistings',
            name='time',
            field=models.CharField(default=datetime.datetime(2020, 12, 20, 10, 20, 49, 451481, tzinfo=utc), max_length=64),
        ),
        migrations.AlterField(
            model_name='comments',
            name='time',
            field=models.CharField(default=datetime.datetime(2020, 12, 20, 10, 20, 49, 452709, tzinfo=utc), max_length=64),
        ),
    ]