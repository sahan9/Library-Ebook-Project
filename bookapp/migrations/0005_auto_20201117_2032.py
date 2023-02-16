# Generated by Django 2.2.9 on 2020-11-17 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0004_auto_20201117_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 17, 15, 2, 21, 254561, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('A', 'Arts & Music'), ('B', 'Biographies'), ('BA', 'Business'), ('C', 'Comics'), ('CM', 'Computers & tech'), ('E', 'Edu & Reference'), ('H', 'History'), ('HR', 'Horror'), ('M', 'Mysterise'), ('R', 'Religion'), ('RM', 'Romance')], max_length=2),
        ),
    ]