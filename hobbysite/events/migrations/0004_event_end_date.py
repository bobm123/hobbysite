# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20150904_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2015, 9, 4, 12, 18, 26, 759000, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
