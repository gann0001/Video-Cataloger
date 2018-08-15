import time
from behave import step
from django.utils import timezone

from toolkit.helpers.bdd import fill_and_submit_form, click_element_by_name
from toolkit.helpers.bdd.shared_steps import *

from people.models import PersonRole

@step('I submit valid role information')
def submit_valid_role(context):
    b = context.browser
    b.fill('name','new role')
    b.find_by_name('submit').click()

@step('I should see the new role')
def valid_role(context):
    assert context.browser.is_text_present('new role')

@step('I have a role')
def tag_available(context):
    context.test_obj = PersonRole.objects.create(name="brand new")
    context.test_obj.save()

@step('I submit updated role information')
def submit_updated_role(context):
    b = context.browser
    b.fill('name', 'candidate')
    b.find_by_name('submit').click()

@step('I should see the updated role')
def validate_updated_role(context):
    assert context.browser.is_text_present('candidate')

@step('I delete the role')
def delete_role(context):
    b = context.browser
    b.find_by_name('submit').click()

@step('I shouldnt see the role')
def validation_role(context):
    assert not context.browser.is_text_present('candidate')

@step('I use the role simple search')
def role_simple_search(context):
    b = context.browser
    context.search_term = PersonRole.objects.first().name
    b.fill('search', context.search_term)
    b.find_by_name('submit_search').click()

@step('I should see the role')
def verify_role_search(context):
    assert context.browser.is_text_present(context.search_term)