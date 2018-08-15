import uuid

from django.core.management import call_command
from toolkit.helpers.bdd import setup_test_environment, flush_context
from toolkit.helpers.utils import snakify


# The scenario param is used behind the scenes
def before_scenario(context, scenario):
    setup_test_environment(context, scenario)
    call_command('loaddata', 'auth.json')


def after_step(context, step):
    # Take a screenshot if the step failed
    if step.status == "failed":
        file_path = '%s_%s_error.png' % (snakify(context.scenario), snakify(step.name))
        context.browser.driver.save_screenshot(file_path)


def after_scenario(context, scenario):
    flush_context(context, scenario)