# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
