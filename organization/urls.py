from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from organization.views import PartyListView, PartyCreateView, PartyDetailView, PartyUpdateView, PartyDeleteView, \
    OrganizationListView, OrganizationCreateView, OrganizationDetailView, OrganizationUpdateView, \
    OrganizationDeleteView, OfficeListView, OfficeCreateView, OfficeDetailView, OfficeUpdateView, OfficeDeleteView

urlpatterns = [

    url(r'^organization/$', login_required(OrganizationListView.as_view()), name='browse_organization'),
    url(r'^organization/add/', login_required(OrganizationCreateView.as_view()), name='add_organization'),
    url(r'^organization/(?P<pk>\d+)/', include([
        url(r'^$', login_required(OrganizationDetailView.as_view()), name='view_organization'),
        url(r'^edit/$', login_required(OrganizationUpdateView.as_view()), name='edit_organization'),
        url(r'^delete/$', login_required(OrganizationDeleteView.as_view()), name='delete_organization'),
    ])),

    url(r'^party/$', login_required(PartyListView.as_view()), name='browse_party'),
    url(r'^party/add/', login_required(PartyCreateView.as_view()), name='add_party'),
    url(r'^party/(?P<pk>\d+)/', include([
        url(r'^$', login_required(PartyDetailView.as_view()), name='view_party'),
        url(r'^edit/$', login_required(PartyUpdateView.as_view()), name='edit_party'),
        url(r'^delete/$', login_required(PartyDeleteView.as_view()), name='delete_party'),
    ])),

    url(r'^office/$', login_required(OfficeListView.as_view()), name='browse_office'),
    url(r'^office/add/', login_required(OfficeCreateView.as_view()), name='add_office'),
    url(r'^office/(?P<pk>\d+)/', include([
        url(r'^$', login_required(OfficeDetailView.as_view()), name='view_office'),
        url(r'^edit/$', login_required(OfficeUpdateView.as_view()), name='edit_office'),
        url(r'^delete/$', login_required(OfficeDeleteView.as_view()), name='delete_office'),
    ])),
]
