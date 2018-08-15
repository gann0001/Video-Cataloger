import time

import arrow
from behave import step

from toolkit.helpers.bdd import fill_and_submit_form, click_element_by_name, settings
from toolkit.helpers.bdd.shared_steps import *

from video.models import Video
from organization.models import Organization,Party,Office
from taxonomy.models import Tag,ElectionYear,VideoFormat
from people.models import PersonRole

@step("I have a organization, party, office, tag, electionyear, videoformat and personrole")
def create_necessary_objects(context):
    context.test_organization = Organization.objects.create(name="Trump Org")
    context.test_party = Party.objects.create(name="Trump Party")
    context.test_office = Office.objects.create(name="CCEIT")
    context.test_tags = [Tag.objects.create(name="test tag")]
    context.test_electionyear = ElectionYear.objects.create(year=1991)
    context.test_videoformat = VideoFormat.objects.create(name="MP4")
    context.test_personrole = PersonRole.objects.create(name="Developer")

@step("I submit valid video information")
def submit_video_info(context):
    b = context.browser
    fields = [
        {'function': 'fill', 'name': 'database_id', 'value': 11},
        {'function': 'fill', 'name': 'original_id', 'value': 20},
        {'function': 'fill', 'name': 'preservation_copy', 'value': 'pcopy10'},
        {'function': 'fill', 'name': 'political_commercial_archive', 'value': 'pca'},
        {'function': 'fill', 'name': 'slate', 'value': 'slate'},
        {'function': 'fill', 'name': 'creation_date', 'value': arrow.now().format('MM/DD/YYYY')},
        {'function': 'select', 'name': 'communication_type', 'value': 'image'},
        {'function': 'select', 'name': 'program_type', 'value': 'commercial'},
        {'function': 'select', 'name': 'election_year', 'value': context.test_electionyear.pk},
        {'function': 'select', 'name': 'format', 'value': context.test_videoformat.pk},
        {'function': 'fill', 'name': 'agency', 'value': 'Sumith'},
        {'function': 'fill', 'name': 'length', 'value': '20'},
        {'function': 'fill', 'name': 'begin_time', 'value': '00:30'},
        {'function': 'fill', 'name': 'first_name', 'value': 'Nathan'},
        {'function': 'fill', 'name': 'last_name', 'value': 'N'},
        {'function': 'fill', 'name': 'organization', 'value': 'CCEIT'},
        {'function': 'select', 'name': 'role', 'value': context.test_personrole.pk},
        {'function': 'select', 'name': 'country', 'value': 'United States of America'},
        {'function': 'select', 'name': 'party', 'value': context.test_party.pk},
        {'function': 'select', 'name': 'state', 'value': 'oklahoma'},
        {'function': 'select', 'name': 'office', 'value': context.test_office.pk},
        {'function': 'select', 'name': 'gender', 'value': 'male'},
        {'function': 'fill', 'name': 'title', 'value': 'Developer'},
        {'function': 'fill', 'name': 'notes', 'value': 'Develops web applications'},
        {'function': 'fill', 'name': 'summary', 'value': 'Fantastic Developer'},
        {'function': 'fill', 'name': 'transcript', 'value': 'no transcript available'},
        {'function': 'fill', 'name': 'subject1', 'value': 'Nathan'},
        {'function': 'fill', 'name': 'subject2', 'value': 'Smith'},
        {'function': 'fill', 'name': 'subject3', 'value': 'CCE-IT'},
        {'function': 'fill', 'name': 'cataloged_date', 'value': arrow.now().format('MM/DD/YYYY')},
        {'function': 'fill', 'name': 'donor', 'value': 'USA'},
        {'function': 'fill', 'name': 'licence', 'value': 'Yes'},
        {'function': 'fill', 'name': 'cataloger', 'value': 'Sumith Gannarapu'},

    ]

    for obj in context.test_tags:
        b.select('tags', obj.pk)
        
    fill_and_submit_form(b, fields)


@step("I should see the new video")
def verify_video_created(context):
    assert context.browser.is_text_present("pcopy10")


@step("I have a video")
def video_available(context):
    context.execute_steps(u'''
        Given I have a organization, party, office, tag, electionyear, videoformat and personrole
    ''')

    context.test_obj = obj = Video.objects.create(
        database_id="11",
        original_id="11",
        preservation_copy='pcopy11',
        political_commercial_archive='pca',
        slate='CCEIT',
        creation_date=arrow.now().date(),
        communication_type=Video.POSITIVE_IMAGE,
        program_type='commercial',
        election_year=context.test_electionyear,
        format=context.test_videoformat,
        agency='agency1',
        length='30',
        begin_time='00:30',
        first_name='Sumith',
        last_name='Gannarapu',
        organization='CCEIT',
        role=context.test_personrole,
        country='United States of America',
        party=context.test_party,
        state='oklahoma',
        office=context.test_office,
        gender='male',
        title='Developer',
        notes='Develops web apps',
        summary='no summary',
        transcript='no transcript',
        subject1='1',
        subject2='2',
        subject3='3',
        cataloged_date=arrow.now().date(),
        donor='sumith',
        licence='yes',
        cataloger='Sumith',
    )

    for tag in context.test_tags:
        obj.tags.add(tag)


@step('I submit updated video information')
def video_edit_update(context):
    b = context.browser
    fields = [
        {'function': 'fill', 'name': 'database_id', 'value': 11},
        {'function': 'fill', 'name': 'original_id', 'value': 20},
        {'function': 'fill', 'name': 'preservation_copy', 'value': 'pcopy10'},
        {'function': 'fill', 'name': 'political_commercial_archive', 'value': 'pca'},
        {'function': 'fill', 'name': 'slate', 'value': 'slate'},
        {'function': 'fill', 'name': 'creation_date', 'value': arrow.now().format('MM/DD/YYYY')},
        {'function': 'select', 'name': 'communication_type', 'value': 'image'},
        {'function': 'select', 'name': 'program_type', 'value': 'commercial'},
        {'function': 'select', 'name': 'election_year', 'value': context.test_electionyear.pk},
        {'function': 'select', 'name': 'format', 'value': context.test_videoformat.pk},
        {'function': 'fill', 'name': 'agency', 'value': 'Sumith'},
        {'function': 'fill', 'name': 'length', 'value': '20'},
        {'function': 'fill', 'name': 'begin_time', 'value': '00:30'},
        {'function': 'fill', 'name': 'first_name', 'value': 'Nathan'},
        {'function': 'fill', 'name': 'last_name', 'value': 'N'},
        {'function': 'fill', 'name': 'organization', 'value': 'CCEIT'},
        {'function': 'select', 'name': 'role', 'value': context.test_personrole.pk},
        {'function': 'select', 'name': 'country', 'value': 'United States of America'},
        {'function': 'select', 'name': 'party', 'value': context.test_party.pk},
        {'function': 'select', 'name': 'state', 'value': 'oklahoma'},
        {'function': 'select', 'name': 'office', 'value': context.test_office.pk},
        {'function': 'select', 'name': 'gender', 'value': 'male'},
        {'function': 'fill', 'name': 'title', 'value': 'Developer'},
        {'function': 'fill', 'name': 'notes', 'value': 'Develops web applications'},
        {'function': 'fill', 'name': 'summary', 'value': 'Fantastic Developer'},
        {'function': 'fill', 'name': 'transcript', 'value': 'no transcript available'},
        {'function': 'fill', 'name': 'subject1', 'value': 'Nathan'},
        {'function': 'fill', 'name': 'subject2', 'value': 'Smith'},
        {'function': 'fill', 'name': 'subject3', 'value': 'CCE-IT'},
        {'function': 'fill', 'name': 'cataloged_date', 'value': arrow.now().format('MM/DD/YYYY HH:mm:ss')},
        {'function': 'fill', 'name': 'donor', 'value': 'USA'},
        {'function': 'fill', 'name': 'licence', 'value': 'Yes'},
        {'function': 'fill', 'name': 'cataloger', 'value': 'Sumith Gannarapu'},
    ]

    fill_and_submit_form(b, fields)

@step("I should see the updated video")
def verify_video_updated(context):
    obj = Video.objects.get(pk=context.test_obj.pk)
    assert context.browser.is_text_present(str(obj.database_id))
    assert context.browser.is_text_present(obj.summary)
    assert context.browser.is_text_present(obj.title)


@step('I delete the video')
def video_delete(context):
    b = context.browser
    context.vid_count = Video.objects.count()
    click_element_by_name(b,'submit')


@step('I shouldnt see the video')
def verify_video_delete(context):
    assert not context.browser.is_text_present("PCOPY 5")
    assert Video.objects.count() < context.vid_count


@step('I use the video simple search')
def search_for_video(context):
    b = context.browser
    database_id = Video.objects.first().database_id
    b.fill('search',database_id)
    b.find_by_name('submit_search')[0].click()


@step('I should see the video')
def verify_video_search_advanced(context):
    assert context.browser.is_text_present("pcopy")


@step('I use the video advanced search')
def advanced_search_for_video(context):
    b = context.browser
    b.find_by_id('advance_search_toggle').click()
    b.fill('first_name','Sumith')
    b.find_by_name('advanced_search').click()
