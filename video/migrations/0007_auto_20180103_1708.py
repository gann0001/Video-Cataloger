# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_auto_20171208_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='cataloged_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='communication_type',
            field=models.CharField(max_length=50, choices=[(b'image', b'Image'), (b'positive', b'Positive'), (b'negative', b'Negative'), (b'positive_image', b'Positive Image'), (b'positive_issue', b'Positive Issue'), (b'negative_image', b'Negative Image'), (b'negative_issue', b'Negative Issue'), (b'issue', b'Issue'), (b'other', b'other')]),
        ),
        migrations.AlterField(
            model_name='video',
            name='creation_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='state',
            field=models.CharField(max_length=50, choices=[(b'alabama', b'Alabama'), (b'alaska', b'Alaska'), (b'american_samoa', b'American Samoa'), (b'arizona', b'Arizona'), (b'arkansas', b'Arkansas'), (b'california', b'California'), (b'colorado', b'Colorado'), (b'connecticut', b'Connecticut'), (b'delaware', b'Delaware'), (b'washington_district_of_columbia', b'Washington District of Columbia'), (b'federated_states_of_micronesia', b'Federated States of Micronesia'), (b'florida', b'Florida'), (b'georgia', b'Georgia'), (b'guam', b'Guam'), (b'hawaii', b'Hawaii'), (b'idaho', b'Idaho'), (b'illinois', b'Illinois'), (b'indiana', b'Indiana'), (b'iowa', b'Iowa'), (b'kansas', b'Kansas'), (b'kentucky', b'Kentucky'), (b'louisiana', b'Louisiana'), (b'maine', b'Maine'), (b'marshall_islands', b'Marshall Islands'), (b'maryland', b'Maryland'), (b'massachusetts', b'Massachusetts'), (b'michigan', b'Michigan'), (b'minnesota', b'Minnesota'), (b'mississippi', b'Mississippi'), (b'missouri', b'Missouri'), (b'montana', b'Montana'), (b'nebraska', b'Nebraska'), (b'nevada', b'Nevada'), (b'new_hampshire', b'New Hampshire'), (b'new_jersey', b'New Jersey'), (b'new_mexico', b'New Mexico'), (b'new_york', b'New York'), (b'north_carolina', b'North Carolina'), (b'north_dakota', b'North Dakota'), (b'northern_mariana_islands', b'Northern Mariana Islands'), (b'ohio', b'Ohio'), (b'oklahoma', b'Oklahoma'), (b'ontario', b'Ontario'), (b'oregon', b'Oregon'), (b'palau', b'Palau'), (b'pennsylvania', b'Pennsylvania'), (b'puerto_rico', b'Puerto Rico'), (b'rhode_island', b'Rhode Island'), (b'rhode_island', b'Rhode Island'), (b'sint_marten', b'Sint Maarten'), (b'south_carikuba', b'South Carolina'), (b'south_dakota', b'South Dakota'), (b'tennessee', b'Tennessee'), (b'texas', b'Texas'), (b'utah', b'Utah'), (b'vermont', b'Vermont'), (b'virgin_islands', b'Virgin Islands'), (b'virginia', b'Virginia'), (b'washington', b'Washington'), (b'west_virginia', b'West Virginia'), (b'wisconsin', b'Wisconsin'), (b'wyoming', b'Wyoming'), (b'west_germany', b'West Germany'), (b'other', b'Other')]),
        ),
    ]
