from django.contrib.auth.models import User
from toolkit.forms import CCEModelForm, CCESimpleSearchForm, CCEModelSearchForm, forms
from organization.models import Party, Organization, Office


class OrganizationForm(CCEModelForm):
    name = forms.CharField(label = 'Organization Name')
    class Meta:
        model = Organization
        fields = ('name',)


class OrganizationSimpleSearch(CCESimpleSearchForm):
    """Simple Search Form Organization"""
    search_placeholder = "Search Organization"

    class Meta(CCESimpleSearchForm.Meta):
        model = Organization
        field_lookups = {'search': ('name__icontains',
                                    )
                         }


class PartyForm(CCEModelForm):
    name = forms.CharField(label = 'Party Name')
    class Meta:
        model = Party
        fields = ('name',)


class PartySimpleSearch(CCESimpleSearchForm):
    """Simple Search Form Party"""
    search_placeholder = 'Search Party'

    class Meta(CCESimpleSearchForm.Meta):
        model = Party
        field_lookups = {'search': ('name__icontains',
                                    )
                         }


class OfficeForm(CCEModelForm):
    name = forms.CharField(label = 'Office Name')
    class Meta:
        model = Office
        fields = ('name',)


class OfficeSimpleSearch(CCESimpleSearchForm):
    """Simple Search Form Party"""
    search_placeholder = 'Search Office'

    class Meta(CCESimpleSearchForm.Meta):
        model = Office
        field_lookups = {
            'search': ('name__icontains',)
        }