# Generated by Django 2.2.1 on 2019-06-05 07:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190529_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='arrival_time',
            field=models.DurationField(blank=True, default=datetime.timedelta(seconds=300), null=True, verbose_name='Arrival time'),
        ),
    ]
