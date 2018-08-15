from django.contrib.auth.models import User
from toolkit.forms import CCEModelForm, CCESimpleSearchForm, CCEModelSearchForm, forms
from taxonomy.models import Tag, ElectionYear, VideoFormat


class TagForm(CCEModelForm):
    name = forms.CharField(label = 'Tag Name')

    class Meta:
        model = Tag
        fields = ('name',)


class TagSimpleSearch(CCESimpleSearchForm):
    """Simple Search Form Tag"""
    search_placeholder = "Search Tag"

    class Meta(CCESimpleSearchForm.Meta):
        model = Tag
        field_lookups = {'search': ('name__icontains',
                                    )
        }


class ElectionYearForm(CCEModelForm):
    year = forms.CharField(label = 'Election Year')

    class Meta:
        model = ElectionYear
        fields = ('year',)


class ElectionYearSimpleSearch(CCESimpleSearchForm):
    """Simple Search Form ElectionYear"""
    search_placeholder = "Search Election Year"

    class Meta(CCESimpleSearchForm.Meta):
        model = ElectionYear
        field_lookups = {'search': ('year__icontains',
                                    )
        }


class VideoFormatForm(CCEModelForm):
    name = forms.CharField(label = 'Video Format Name')

    class Meta:
        model = VideoFormat
        fields = ('name',)


class VideoFormatSimpleSearch(CCESimpleSearchForm):
    """Simple Search Form ElectionYear"""
    search_placeholder = "Search format name"

    class Meta(CCESimpleSearchForm.Meta):
        model = VideoFormat
        field_lookups = {'search': ('name__icontains',
                                    )
        }