# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRatingStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True, unique=True)),
                ('average', models.DecimalField(max_digits=3, decimal_places=1)),
                ('median', models.DecimalField(max_digits=3, decimal_places=1)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
