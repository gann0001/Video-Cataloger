# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import toolkit.models.mixins
from django.conf import settings
import cuser.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('created_by', cuser.fields.CurrentUserField(related_name='organization_office_last_created', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('last_updated_by', cuser.fields.CurrentUserField(related_name='organization_office_last_updated', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(toolkit.models.mixins.ModelPermissionsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('created_by', cuser.fields.CurrentUserField(related_name='organization_organization_last_created', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('last_updated_by', cuser.fields.CurrentUserField(related_name='organization_organization_last_updated', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(toolkit.models.mixins.ModelPermissionsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('created_by', cuser.fields.CurrentUserField(related_name='organization_party_last_created', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('last_updated_by', cuser.fields.CurrentUserField(related_name='organization_party_last_updated', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(toolkit.models.mixins.ModelPermissionsMixin, models.Model),
        ),
    ]
