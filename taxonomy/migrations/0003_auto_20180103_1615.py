# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0002_auto_20171208_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionyear',
            name='year',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
