# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20150602_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklyrating',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
