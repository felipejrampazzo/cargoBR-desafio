# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0002_auto_20150916_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='id',
            field=models.CharField(editable=False, primary_key=True, serialize=False, max_length=6),
        ),
    ]
