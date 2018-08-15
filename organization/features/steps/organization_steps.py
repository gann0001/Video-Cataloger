import time
from behave import step
from django.utils import timezone

from toolkit.helpers.bdd import fill_and_submit_form, click_element_by_name
from toolkit.helpers.bdd.shared_steps import *

from organization.models import Party, Organization, Office


@step('I submit valid party information')
def submit_party_info(context):
    b = context.browser
    b.fill('name','Janasena Party')
    b.find_by_name('submit').click()


@step('I should see the new party')
def verify_new_party(context):
    assert context.browser.is_text_present('Party')


@step('I (have|should see) a party')
def party_available(context,_ ):
    context.test_obj = Party.objects.create(name="congress party")
    context.test_obj.save()


@step('I submit updated party information')
def update_party_info(context):
    b = context.browser
    b.fill('name', 'BJP')
    b.find_by_name('submit').click()


@step('I should see the updated party')
def verify_update_party(context):
    assert context.browser.is_text_present('BJP')


@step('I delete the party')
def delete_party(context):
    b = context.browser
    b.find_by_name('submit').click()


@step('I shouldnt see the party')
def verify_delete_party(context):
    assert not context.browser.is_text_present('BJP')


@step('I use the party simple search')
def party_simple_search(context):
    b = context.browser
    context.search_term = Party.objects.first().name
    b.fill('search', context.search_term)
    b.find_by_name('submit_search').click()


@step('I should see the party')
def verify_party_search(context):
    assert context.browser.is_text_present(context.search_term)

#Organization

@step('I submit valid organization information')
def submit_organization_info(context):
    b = context.browser
    b.fill('name','Hilary Organization')
    b.find_by_name('submit').click()


@step('I should see the new organization')
def verify_new_organization(context):
    assert context.browser.is_text_present('Hilary')


@step('I (have|should see) a organization')
def organization_available(context,_ ):
    context.test_obj = Organization.objects.create(name="Trump Organization")
    context.test_obj.save()


@step('I submit updated organization information')
def update_organization_info(context):
    b = context.browser
    b.fill('name', 'Obama Organization')
    b.find_by_name('submit').click()


@step('I should see the updated organization')
def verify_update_organization(context):
    assert context.browser.is_text_present('Obama')


@step('I delete the organization')
def delete_party(context):
    b = context.browser
    b.find_by_name('submit').click()


@step('I shouldnt see the organization')
def verify_delete_party(context):
    assert not context.browser.is_text_present('Obama')


@step('I use the organization simple search')
def organization_simple_search(context):
    b = context.browser
    context.search_term = Organization.objects.first().name
    b.fill('search', context.search_term)
    b.find_by_name('submit_search').click()


@step('I should see the organization')
def verify_organization_search(context):
    assert context.browser.is_text_present(context.search_term)

# Office


@step('I submit valid office information')
def submit_office_info(context):
    b = context.browser
    b.fill('name','CCEIT')
    b.find_by_name('submit').click()


@step('I should see the new office')
def verify_new_office(context):
    assert context.browser.is_text_present('CCEIT')


@step('I (have|should see) a office')
def office_available(context,_ ):
    context.test_obj = Office.objects.create(name="PCC")
    context.test_obj.save()


@step('I submit updated office information')
def update_office_info(context):
    b = context.browser
    b.fill('name', 'ARC')
    b.find_by_name('submit').click()


@step('I should see the updated office')
def verify_update_office(context):
    assert context.browser.is_text_present('ARC')


@step('I delete the office')
def delete_office(context):
    b = context.browser
    b.find_by_name('submit').click()


@step('I shouldnt see the office')
def verify_delete_office(context):
    assert not context.browser.is_text_present('ARC')


@step('I use the office simple search')
def office_simple_search(context):
    b = context.browser
    context.search_term = Office.objects.first().name
    b.fill('search', context.search_term)
    b.find_by_name('submit_search').click()


@step('I should see the office')
def verify_office_search(context):
    assert context.browser.is_text_present(context.search_term)

