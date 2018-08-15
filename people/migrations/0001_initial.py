# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import cuser.fields
import toolkit.models.mixins


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(max_length=20)),
                ('created_by', cuser.fields.CurrentUserField(related_name='people_personrole_last_created', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('last_updated_by', cuser.fields.CurrentUserField(related_name='people_personrole_last_updated', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(toolkit.models.mixins.ModelPermissionsMixin, models.Model),
        ),
    ]
