from toolkit.views import CCECreateView, reverse, CCEDeleteView, \
    CCEUpdateView, CCEListView, CCEDetailView, ReportDownloadSearchView, OrderedDict, CCEFormView, messages
from toolkit.views import CCESearchView
from toolkit.views import CCETemplateView

from video.forms import VideoForm, VideoSimpleSearch, VideoAdvancedSearchForm, CommentForm, ImportVideosForm
from .models import Video, Comment


class VideoListView(ReportDownloadSearchView):
    model = Video
    page_title = 'Video Cataloger'
    search_form_class = VideoSimpleSearch
    advanced_search_form_class = VideoAdvancedSearchForm
    sidebar_group = ['Video',]
    columns = [
        ('Database Id', 'database_id'),
        ('Original Id', 'original_id'),
        ('Title', 'title'),
        ('First Name', 'first_name'),
        ('Last Name', 'last_name'),
        ('Office', 'office'),
        ('State', 'state'),
        ('Party', 'party'),
        ('Election Year', 'election_year'),

    ]
    paginate_by = 20
    show_context_menu = True

    def get_reports(self):
        reports = OrderedDict()
        reports['video_xlsx_export'] = {
            'name': 'Export Video (XLSX)',
            'method': 'video_xlsx_export'
        }
        return reports


class VideoCreateView(CCECreateView):
    model = Video
    form_class = VideoForm
    page_title = "Create a New Video!"
    sidebar_group = ['Video', ]
    success_message = "Video Created Successfully"
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_videos')


class VideoDetailView(CCEDetailView):
    model = Video
    page_title = "Video Detail"
    template_name = 'video_detail.html'
    sidebar_group = ['Video',]
    detail_fields = [
        ('Database Id', 'database_id'),
        ('Original Id', 'original_id'),
        ('Preservation Copy', 'preservation_copy'),
        ('Political Commercial Archive', 'political_commercial_archive'),
        ('Slate', 'slate'),
        ('Creation Date', 'creation_date'),
        ('Communication Type', 'communication_type'),
        ('Program Type', 'program_type'),
        ('Election Year', 'election_year'),
        ('Format', 'format'),
        ('Agency', 'agency'),
        ('Length', 'length'),
        ('Begin Time', 'begin_time'),
        ('First Name', 'first_name'),
        ('Last Name', 'last_name'),
        ('Organization', 'organization'),
        ('Role', 'role'),
        ('Country', 'country'),
        ('Party', 'party'),
        ('State', 'state'),
        ('Office', 'office'),
        ('Gender', 'gender'),
        ('Title', 'title'),
        ('Notes', 'notes'),
        ('Summary', 'summary'),
        ('Transcript', 'transcript'),
        ('Subject1', 'subject1'),
        ('Subject2', 'subject2'),
        ('Subject3', 'subject3'),
        ('Cataloged Date', 'cataloged_date'),
        ('Donor', 'donor'),
        ('Licence', 'licence'),
        ('Cataloger', 'cataloger'),
        ('Tags', 'tags'),
    ]
    show_context_menu = True


class VideoUpdateView(CCEUpdateView):
    model = Video
    page_title = "Edit Video"
    sidebar_group = ['Video',]
    form_class = VideoForm
    success_message = "Video Edited Succesfully"
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_videos')


class VideoDeleteView(CCEDeleteView):
    model = Video
    page_title = 'Delete Video'
    sidebar_group = ['Video',]
    success_message = 'Video Deleted Succesfully'

    def get_success_url(self):
        return reverse('browse_videos')


class CommentCreateView(CCECreateView):
    model = Comment
    sidebar_group = ['Video',]
    form_class = CommentForm
    page_title = "Create Comment"
    success_message = "Comment created succesfully"
    show_context_menu = True

    def get_success_url(self):
        return reverse('view_video',kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        result =  super(CommentCreateView, self).get_context_data(**kwargs)
        result['form'] = CommentForm(initial={'video': Video.objects.get(pk=self.kwargs['pk'])})
        return result


class VideoImportView(CCEFormView):
    page_title = "Import Videos"
    page_icon = 'fa fa-upload'
    form_class = ImportVideosForm
    sidebar_group = ['Video',]
    template_name = 'import.html'

    def get_success_url(self):
        return reverse('browse_videos')

    def form_valid(self, form):
        xlsxfile = self.request.FILES['file']
        created_list, updated_list, error_list = Video.import_videos(xlsxfile)
        if error_list:
            messages.warning(self.request, '\n'.join(error_list))
        if created_list:
            messages.success(self.request, '\n'.join(created_list))
        if updated_list:
            messages.success(self.request, '\n'.join(updated_list))
        return super(VideoImportView, self).form_valid(form)






