# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_auto_20171208_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cataloged_date',
            field=models.DateTimeField(),
        ),
    ]
