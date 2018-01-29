from toolkit.views import CCECreateView, reverse, CCEDeleteView, \
    CCEUpdateView, CCEListView, CCEDetailView
from toolkit.views import CCESearchView
from toolkit.views import CCETemplateView

from organization.forms import PartyForm, PartySimpleSearch, OrganizationSimpleSearch, OrganizationForm, OfficeForm, OfficeSimpleSearch
from .models import Party, Organization, Office


class OrganizationListView(CCESearchView):
    model = Organization
    page_title = 'Browse Organization'
    sidebar_group = ['Organization',]
    search_form_class = OrganizationSimpleSearch
    columns = [
        ('Party Name', 'name')
    ]
    show_context_menu = True


class OrganizationCreateView(CCECreateView):
    model = Organization
    sidebar_group = ['Organization',]
    form_class = OrganizationForm
    page_title = 'Create Organization'
    success_message = 'Organization Created Successfully'

    def get_success_url(self):
        return reverse('browse_organization')
    show_context_menu = True


class OrganizationDetailView(CCEDetailView):
    model = Organization
    sidebar_group = ['Organization',]
    page_title = 'Organization Details'
    detail_fields = [
        ('Organization Name','name')
    ]
    show_context_menu = True


class OrganizationUpdateView(CCEUpdateView):
    model = Organization
    sidebar_group = ['Organization',]
    page_title = 'Edit Organization'
    show_context_menu = True
    form_class = OrganizationForm
    success_message = 'Organization Edited Successfully'
    def get_success_url(self):
        return reverse('browse_organization')


class OrganizationDeleteView(CCEDeleteView):
    model = Organization
    sidebar_group = ['Organization']
    page_title = 'Delete Organization'
    success_message = 'Organization Deleted Successfully'

    def get_success_url(self):
        return reverse('browse_organization')


class PartyListView(CCESearchView):
    model = Party
    page_title = 'Browse Party'
    search_form_class = PartySimpleSearch
    sidebar_group = ['Organization',]
    columns = [
        ('Party Name','name')
    ]
    paginate_by = 10
    show_context_menu = True


class PartyCreateView(CCECreateView):
    model = Party
    page_title = 'Create Party!'
    form_class = PartyForm
    sidebar_group = ['Organization',]
    success_message = 'Party Created Successfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_party')


class PartyDetailView(CCEDetailView):
    model = Party
    page_title = 'Party Details'
    sidebar_group = ['Organization',]
    detail_fields = [
        ('Party Name', 'name'),
        ]
    show_context_menu = True


class PartyUpdateView(CCEUpdateView):
    model = Party
    page_title = 'Edit Party'
    sidebar_group = ['Organization',]
    form_class = PartyForm
    success_message = 'Party Edited Successfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_party')


class PartyDeleteView(CCEDeleteView):
    model = Party
    page_title = 'Delete Party'
    sidebar_group = ['Organization',]
    success_message = 'Party Deleted Successfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_party')


class OfficeListView(CCESearchView):
    model = Office
    page_title = 'Browse Office'
    search_form_class = OfficeSimpleSearch
    sidebar_group = ['Organization',]
    columns = [
        ('Office Name','name')
    ]
    paginate_by = 10
    show_context_menu = True


class OfficeCreateView(CCECreateView):
    model = Office
    page_title = 'Create Office!'
    form_class = OfficeForm
    sidebar_group = ['Organization',]
    success_message = 'Office Created Successfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_office')


class OfficeDetailView(CCEDetailView):
    model = Office
    page_title = 'Office Details'
    sidebar_group = ['Organization',]
    detail_fields = [
        ('Party Name', 'name')
    ]
    show_context_menu = True


class OfficeUpdateView(CCEUpdateView):
    model = Office
    page_title = 'Edit Office'
    sidebar_group = ['Organization',]
    form_class = PartyForm
    success_message = 'Office Edited Successfully'

    def get_success_url(self):
        return reverse('browse_office')


class OfficeDeleteView(CCEDeleteView):
    model = Office
    page_title = 'Delete Office'
    sidebar_group = ['Organization']
    success_message = 'Office Deleted Succesfully'

    def get_success_url(self):
        return reverse('browse_office')
