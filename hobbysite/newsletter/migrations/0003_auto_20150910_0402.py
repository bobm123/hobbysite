# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_remove_newsletter_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='pdf',
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
