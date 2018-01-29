# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20171208_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='agency',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='cataloger',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='communication_type',
            field=models.CharField(max_length=50, choices=[(b'image', b'Image'), (b'positive_image', b'Positive Image'), (b'positive_issue', b'Positive Issue'), (b'negative_image', b'Negative Image'), (b'negative_issue', b'Negative Issue'), (b'issue', b'Issue')]),
        ),
        migrations.AlterField(
            model_name='video',
            name='donor',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='first_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='last_name',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='licence',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='organization',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='program_type',
            field=models.CharField(max_length=50, choices=[(b'commercial', b'Commercial'), (b'convention', b'Convention'), (b'debate', b'Debate'), (b'interview', b'Interview'), (b'news', b'News'), (b'program', b'Program'), (b'public_service_announcement', b'Public Service Announcement'), (b'rally', b'Rally'), (b'speech', b'Speech'), (b'other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='video',
            name='summary',
            field=models.TextField(max_length=9000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='transcript',
            field=models.TextField(max_length=9000, null=True, blank=True),
        ),
    ]
