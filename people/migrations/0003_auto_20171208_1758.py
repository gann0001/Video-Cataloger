# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20171208_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personrole',
            name='name',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
