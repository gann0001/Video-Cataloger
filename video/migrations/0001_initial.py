# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
from django.conf import settings
import django.utils.timezone
import toolkit.models.mixins
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=25)),
                ('comment', models.TextField(max_length=250)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', cuser.fields.CurrentUserField(related_name='video_comment_last_created', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('last_updated_by', cuser.fields.CurrentUserField(related_name='video_comment_last_updated', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(toolkit.models.mixins.ModelPermissionsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('database_id', models.IntegerField(unique=True)),
                ('original_id', models.IntegerField(unique=True)),
                ('preservation_copy', models.CharField(max_length=25, blank=True)),
                ('political_commercial_archive', models.CharField(max_length=25, blank=True)),
                ('slate', models.CharField(max_length=25, blank=True)),
                ('creation_date', models.DateField(default=django.utils.timezone.now)),
                ('communication_type', models.CharField(max_length=25, choices=[(b'image', b'Image'), (b'positive_image', b'Positive Image'), (b'positive_issue', b'Positive Issue'), (b'negative_image', b'Negative Image'), (b'negative_issue', b'Negative Issue'), (b'issue', b'Issue')])),
                ('program_type', models.CharField(max_length=25, choices=[(b'commercial', b'Commercial'), (b'convention', b'Convention'), (b'debate', b'Debate'), (b'interview', b'Interview'), (b'news', b'News'), (b'program', b'Program'), (b'public_service_announcement', b'Public Service Announcement'), (b'rally', b'Rally'), (b'speech', b'Speech'), (b'other', b'Other')])),
                ('agency', models.CharField(max_length=25, null=True, blank=True)),
                ('length', models.CharField(max_length=25, null=True, blank=True)),
                ('begin_time', models.CharField(max_length=25, null=True, blank=True)),
                ('first_name', models.CharField(max_length=25, null=True, blank=True)),
                ('last_name', models.CharField(max_length=25, null=True, blank=True)),
                ('organization', models.CharField(max_length=25, null=True, blank=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', models.CharField(max_length=50, choices=[(b'alabama', b'Alabama'), (b'alaska', b'Alaska'), (b'american_samoa', b'American Samoa'), (b'arizona', b'Arizona'), (b'arkansas', b'Arkansas'), (b'california', b'California'), (b'colorado', b'Colorado'), (b'connecticut', b'Connecticut'), (b'delaware', b'Delaware'), (b'washington_district_of_columbia', b'Washington District of Columbia'), (b'federated_states_of_micronesia', b'Federated States of Micronesia'), (b'florida', b'Florida'), (b'georgia', b'Georgia'), (b'guam', b'Guam'), (b'hawaii', b'Hawaii'), (b'idaho', b'Idaho'), (b'illinois', b'Illinois'), (b'indiana', b'Indiana'), (b'iowa', b'Iowa'), (b'kansas', b'Kansas'), (b'kentucky', b'Kentucky'), (b'louisiana', b'Louisiana'), (b'maine', b'Maine'), (b'marshall_islands', b'Marshall Islands'), (b'maryland', b'Maryland'), (b'massachusetts', b'Massachusetts'), (b'michigan', b'Michigan'), (b'minnesota', b'Minnesota'), (b'mississippi', b'Mississippi'), (b'missouri', b'Missouri'), (b'montana', b'Montana'), (b'nebraska', b'Nebraska'), (b'nevada', b'Nevada'), (b'new_hampshire', b'New Hampshire'), (b'new_jersey', b'New Jersey'), (b'new_mexico', b'New Mexico'), (b'new_york', b'New York'), (b'north_carolina', b'North Carolina'), (b'north_dakota', b'North Dakota'), (b'northern_mariana_islands', b'Northern Mariana Islands'), (b'ohio', b'Ohio'), (b'oklahoma', b'Oklahoma'), (b'ontario', b'Ontario'), (b'oregon', b'Oregon'), (b'palau', b'Palau'), (b'pennsylvania', b'Pennsylvania'), (b'puerto_rico', b'Puerto Rico'), (b'rhode_island', b'Rhode Island'), (b'south_carolina', b'South Carolina'), (b'south_dakota', b'South Dakota'), (b'tennessee', b'Tennessee'), (b'texas', b'Texas'), (b'utah', b'Utah'), (b'vermont', b'Vermont'), (b'virgin_islands', b'Virgin Islands'), (b'virginia', b'Virginia'), (b'washington', b'Washington'), (b'west_virginia', b'West Virginia'), (b'wisconsin', b'Wisconsin'), (b'wyoming', b'Wyoming'), (b'west_germany', b'West Germany'), (b'other', b'Other')])),
                ('gender', models.CharField(max_length=10, choices=[(b'male', b'Male'), (b'female', b'Female'), (b'transgender', b'Transgender'), (b'unknown', b'Unknown')])),
                ('title', models.CharField(max_length=25, null=True, blank=True)),
                ('notes', models.CharField(max_length=100, null=True, blank=True)),
                ('summary', models.TextField(max_length=1000, null=True, blank=True)),
                ('transcript', models.TextField(max_length=1000, null=True, blank=True)),
                ('subject1', models.CharField(max_length=50, null=True, blank=True)),
                ('subject2', models.CharField(max_length=50, null=True, blank=True)),
                ('subject3', models.CharField(max_length=50, null=True, blank=True)),
                ('cataloged_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('donor', models.CharField(max_length=25, null=True, blank=True)),
                ('licence', models.CharField(max_length=25, null=True, blank=True)),
                ('cataloger', models.CharField(max_length=25, null=True, blank=True)),
                ('created_by', cuser.fields.CurrentUserField(related_name='video_video_last_created', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('election_year', models.ForeignKey(related_name='ElectionYear', to='taxonomy.ElectionYear', null=True)),
                ('format', models.ForeignKey(related_name='VideoFormat', to='taxonomy.VideoFormat', null=True)),
                ('last_updated_by', cuser.fields.CurrentUserField(related_name='video_video_last_updated', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('office', models.ForeignKey(related_name='Office', to='organization.Office', null=True)),
                ('party', models.ForeignKey(related_name='Party', to='organization.Party', null=True)),
                ('role', models.ForeignKey(related_name='PersonRole', to='people.PersonRole', null=True)),
                ('tags', models.ManyToManyField(to='taxonomy.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=(toolkit.models.mixins.ModelPermissionsMixin, models.Model),
        ),
        migrations.AddField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(to='video.Video'),
        ),
    ]
