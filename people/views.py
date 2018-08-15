from toolkit.views import CCECreateView, reverse, CCEDeleteView, \
    CCEUpdateView, CCEListView, CCEDetailView
from toolkit.views import CCESearchView
from toolkit.views import CCETemplateView

from people.forms import PersonRoleSimpleSearch, PersonRoleForm
from .models import PersonRole


class PersonRoleListView(CCESearchView):
    model = PersonRole
    page_title = "Browse Person Role"
    sidebar_group = ['People',]
    search_form_class = PersonRoleSimpleSearch
    columns = [
        ('Person Role', 'name')
    ]
    show_context_menu = True


class PersonRoleCreateView(CCECreateView):
    model = PersonRole
    page_title = 'Create Role'
    sidebar_group = ['People',]
    form_class = PersonRoleForm
    success_message = 'Role Created Successfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_person_role')


class PersonRoleDetailView(CCEDetailView):
    model = PersonRole
    page_title = 'Role Details'
    sidebar_group = ['People',]
    detail_fields = [
        ('Person Role', 'name'),
    ]
    show_context_menu = True


class PersonRoleUpdateView(CCEUpdateView):
    model = PersonRole
    page_title = 'Edit Role'
    sidebar_group = ['People',]
    show_context_menu = True
    success_message = 'Role Edited Successfully'
    form_class = PersonRoleForm

    def get_success_url(self):
        return reverse('browse_person_role')


class PersonRoleDeleteView(CCEDeleteView):
    model = PersonRole
    page_title = 'Delete Role'
    sidebar_group = ['People',]
    success_message = 'Role Deleted Successfully'

    def get_success_url(self):
        return reverse('browse_person_role')