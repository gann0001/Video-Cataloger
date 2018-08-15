# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_auto_20180103_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='notes',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='summary',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='transcript',
            field=models.TextField(null=True, blank=True),
        ),
    ]
