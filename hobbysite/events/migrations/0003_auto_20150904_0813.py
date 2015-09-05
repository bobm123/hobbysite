# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150904_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=80),
        ),
    ]
