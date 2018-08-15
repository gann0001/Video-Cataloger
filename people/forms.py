from django.contrib.auth.models import User
from toolkit.forms import CCEModelForm, CCESimpleSearchForm, CCEModelSearchForm, forms
from people.models import PersonRole


class PersonRoleForm(CCEModelForm):
    name = forms.CharField(label = 'Person role')

    class Meta:
        model = PersonRole
        fields = ('name',)


class PersonRoleSimpleSearch(CCESimpleSearchForm):
    """Simple Search Form Person"""
    search_placeholder = "Search Person Role"

    class Meta(CCESimpleSearchForm.Meta):
        model = PersonRole
        field_lookups = {'search': ('name__icontains',
                                    )
        }