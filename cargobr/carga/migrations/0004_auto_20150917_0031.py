# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0003_auto_20150916_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='id',
            field=models.CharField(serialize=False, max_length=6, primary_key=True),
        ),
    ]
