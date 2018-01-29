from django.contrib.auth.models import User
from toolkit.forms import CCEModelForm, CCESimpleSearchForm, CCEModelSearchForm, forms
from video.models import Video, Comment


class VideoForm(CCEModelForm):
    class Meta:
        model = Video
        fields = ('database_id',
                  'original_id',
                  'preservation_copy',
                  'political_commercial_archive',
                  'slate',
                  'creation_date',
                  'communication_type',
                  'program_type',
                  'election_year',
                  'format',
                  'agency',
                  'length',
                  'begin_time',
                  'first_name',
                  'last_name',
                  'organization',
                  'role',
                  'country',
                  'party',
                  'state',
                  'office',
                  'gender',
                  'title',
                  'notes',
                  'summary',
                  'transcript',
                  'subject1',
                  'subject2',
                  'subject3',
                  'cataloged_date',
                  'donor',
                  'licence',
                  'cataloger',
                  'tags',
                  )

class VideoSimpleSearch(CCESimpleSearchForm):
    """Simple Search Form Tasks"""
    search_placeholder = 'Search Video'

    class Meta(CCESimpleSearchForm.Meta):
        model = Video
        field_lookups = {'search': ('original_id',
                                    )}
class VideoAdvancedSearchForm(CCEModelSearchForm):
    """ Advanced Search Form Tasks"""
    #office = forms.CharField(max_length = 100, required = False)
    #state = forms.CharField(max_length = 100, required = False)
    #party = forms.CharField(max_length = 100, required = False)
    created_by = forms.ModelChoiceField(User.objects.all(), required = False)

    class Meta:
        model = Video
        field_lookups = {
            'title': 'title__icontains',
            'first_name': 'first_name__icontains',
            'last_name': 'last_name__icontains',
            'office': 'office',
            'state': 'state',
            'party': 'party',
            'created_by': 'created_by',
        }

        fields = (
            'title',
            'first_name',
            'last_name',
            'office',
            'state',
            'party',
            'created_by',
        )


class CommentForm(CCEModelForm):
    class Meta:
        model = Comment
        fields = ('video',
                  'name',
                  'comment',
                  'created_date',)
        widgets = {'video': forms.HiddenInput}


class ImportVideosForm(CCEModelForm):
    file = forms.FileField(required=True)

    class Meta:
        model = Video
        fields = ()

