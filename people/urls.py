from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from people.views import PersonRoleListView, PersonRoleCreateView, PersonRoleDetailView, PersonRoleUpdateView, \
    PersonRoleDeleteView

urlpatterns = [
        
    url(r'^person_role/$', login_required(PersonRoleListView.as_view()), name='browse_person_role'),
    url(r'^person_role/add/', login_required(PersonRoleCreateView.as_view()), name='add_person_role'),
    url(r'^person_role/(?P<pk>\d+)/', include([
        url(r'^$', login_required(PersonRoleDetailView.as_view()), name='view_person_role'),
        url(r'^edit/$', login_required(PersonRoleUpdateView.as_view()), name='edit_person_role'),
        url(r'^delete/$', login_required(PersonRoleDeleteView.as_view()), name='delete_person_role'),
    ])),

]
