# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.CharField(primary_key=True, editable=False, max_length=6, serialize=False, unique=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dados', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
