# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carga',
            name='id',
            field=models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True),
        ),
    ]
