# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='videoformat',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
