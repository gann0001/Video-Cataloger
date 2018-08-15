import time
from behave import step
from django.utils import timezone

from toolkit.helpers.bdd import fill_and_submit_form, click_element_by_name
from toolkit.helpers.bdd.shared_steps import *

from taxonomy.models import Tag, ElectionYear, VideoFormat

@step('I submit valid tag information')
def submit_valid_tag(context):
    b = context.browser
    b.fill('name','tag 100')
    b.find_by_name('submit').click()

@step('I should see the new tag')
def valid_tag(context):
    assert context.browser.is_text_present('tag 100')

@step('I have a tag')
def tag_available(context):
    context.test_obj = Tag.objects.create(name="new tag")
    context.test_obj.save()

@step('I submit updated tag information')
def submit_updated_tag(context):
    b = context.browser
    b.fill('name', 'tag 99')
    b.find_by_name('submit').click()

@step('I should see the updated tag')
def validate_updated_tag(context):
    assert context.browser.is_text_present('99')

@step('I delete the tag')
def delete_tag(context):
    b = context.browser
    b.find_by_name('submit').click()

@step('I shouldnt see the tag')
def validation_tag(context):
    assert not context.browser.is_text_present('99')

@step('I use the tag simple search')
def tag_simple_search(context):
    b = context.browser
    context.search_term = Tag.objects.first().name
    b.fill('search', context.search_term)
    b.find_by_name('submit_search').click()

@step('I should see the tag')
def verify_tag_search(context):
    assert context.browser.is_text_present(context.search_term)

#Election Year

@step('I submit valid year information')
def submit_valid_year(context):
    b = context.browser
    b.fill('year', 1970)
    b.find_by_name('submit').click()


@step('I should see the new year')
def valid_year(context):
    assert context.browser.is_text_present('1970')


@step('I have a year')
def year_available(context):
    context.test_obj = ElectionYear.objects.create(year=1940)
    context.test_obj.save()


@step('I submit updated year information')
def submit_updated_tag(context):
    b = context.browser
    b.fill('year', 1947)
    b.find_by_name('submit').click()


@step('I should see the updated year')
def validate_updated_year(context):
    assert context.browser.is_text_present('1947')


@step('I delete the year')
def delete_year(context):
    b = context.browser
    b.find_by_name('submit').click()


@step('I shouldnt see the year')
def validation_year(context):
    assert not context.browser.is_text_present('1940')


@step('I use the year simple search')
def year_simple_search(context):
    b = context.browser
    context.search_term = ElectionYear.objects.first().year
    b.fill('search', context.search_term)
    b.find_by_name('submit_search').click()


@step('I should see the year')
def verify_year_search(context):
    assert context.browser.is_text_present(str(context.search_term))

#VideoFormat


@step('I submit valid format information')
def submit_valid_format(context):
    b = context.browser
    b.fill('name', '70 mm film')
    b.find_by_name('submit').click()


@step('I should see the new format')
def valid_format(context):
    assert context.browser.is_text_present('film')


@step('I have a format')
def format_available(context):
    context.test_obj = VideoFormat.objects.create(name='35 mm Film')
    context.test_obj.save()


@step('I submit updated format information')
def submit_updated_format(context):
    b = context.browser
    b.fill('name', '45 mm')
    b.find_by_name('submit').click()


@step('I should see the updated format')
def validate_updated_format(context):
    assert context.browser.is_text_present('45')


@step('I delete the format')
def delete_format(context):
    b = context.browser
    b.find_by_name('submit').click()


@step('I shouldnt see the format')
def validation_format(context):
    assert not context.browser.is_text_present('45')


@step('I use the format simple search')
def format_simple_search(context):
    b = context.browser
    context.search_term = VideoFormat.objects.first().name
    b.fill('search', context.search_term)
    b.find_by_name('submit_search').click()


@step('I should see the format')
def verify_format_search(context):
    assert context.browser.is_text_present(context.search_term)
