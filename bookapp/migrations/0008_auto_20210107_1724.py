# Generated by Django 2.2.9 on 2021-01-07 11:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0007_auto_20201117_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 7, 11, 54, 15, 968040, tzinfo=utc)),
        ),
    ]
