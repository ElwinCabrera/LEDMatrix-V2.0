# Generated by Django 2.2.6 on 2019-11-16 21:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191116_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledmatrixsettings',
            name='led_matrix_off_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2019, 11, 16, 21, 57, 48, 769725, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='ledmatrixsettings',
            name='led_matrix_on_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2019, 11, 16, 21, 57, 48, 769707, tzinfo=utc), null=True),
        ),
    ]
