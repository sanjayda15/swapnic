# Generated by Django 3.0.3 on 2020-07-14 06:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('swapnic_blog', '0006_auto_20200714_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 6, 43, 19, 769524, tzinfo=utc)),
        ),
    ]
