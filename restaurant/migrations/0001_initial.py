# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.IntegerField()),
                ('name', models.CharField(max_length=2000)),
                ('type', models.CharField(max_length=2000)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('location_x', models.FloatField()),
                ('location_y', models.FloatField()),
                ('rc_point', models.FloatField()),
                ('vote', models.FloatField()),
            ],
        ),
    ]
