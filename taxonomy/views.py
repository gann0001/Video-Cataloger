from toolkit.views import CCECreateView, reverse, CCEDeleteView, \
    CCEUpdateView, CCEListView, CCEDetailView
from toolkit.views import CCESearchView
from toolkit.views import CCETemplateView

from taxonomy.forms import TagSimpleSearch, TagForm, ElectionYearForm, ElectionYearSimpleSearch, VideoFormatForm, \
    VideoFormatSimpleSearch
from .models import Tag, ElectionYear, VideoFormat


class TagListView(CCESearchView):
    model = Tag
    page_title = "Browse Tag"
    sidebar_group = ['Taxonomy',]
    search_form_class = TagSimpleSearch
    columns = [
        ('Tag Name', 'name')
    ]
    show_context_menu = True


class TagCreateView(CCECreateView):
    model = Tag
    page_title = 'Create Tag'
    sidebar_group = ['Taxonomy',]
    form_class = TagForm
    success_message = 'Tag Created Succesfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_tag')


class TagDetailView(CCEDetailView):
    model = Tag
    page_title = 'Tag Details'
    sidebar_group = ['Taxonomy',]
    detail_fields = [
        ('Tag Name', 'name'),
    ]
    show_context_menu = True


class TagUpdateView(CCEUpdateView):
    model = Tag
    page_title = 'Edit Tag'
    sidebar_group = ['Taxonomy',]
    show_context_menu = True
    success_message = 'Tag Edited Succesfully'
    form_class = TagForm
    def get_success_url(self):
        return reverse('browse_tag')


class TagDeleteView(CCEDeleteView):
    model = Tag
    page_title = 'Delete Tag'
    sidebar_group = ['Taxonomy',]
    success_message = 'Tag Deleted Succesfully'

    def get_success_url(self):
        return reverse('browse_tag')


class ElectionYearListView(CCESearchView):
    model = ElectionYear
    page_title = "Browse Election Year"
    sidebar_group = ['Taxonomy',]
    search_form_class = ElectionYearSimpleSearch
    columns = [
        ('Election Year', 'year')
    ]
    show_context_menu = True


class ElectionYearCreateView(CCECreateView):
    model = ElectionYear
    page_title = 'Create Election Year'
    sidebar_group = ['Taxonomy',]
    form_class = ElectionYearForm
    success_message = 'Year Created Succesfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_election_year')


class ElectionYearDetailView(CCEDetailView):
    model = ElectionYear
    page_title = 'Election Year Details'
    sidebar_group = ['Taxonomy',]
    detail_fields = [
        ('Election Year', 'year'),
    ]
    show_context_menu = True


class ElectionYearUpdateView(CCEUpdateView):
    model = ElectionYear
    page_title = 'Edit Year'
    sidebar_group = ['Taxonomy',]
    show_context_menu = True
    success_message = 'Year Edited Succesfully'
    form_class = ElectionYearForm
    def get_success_url(self):
        return reverse('browse_election_year')


class ElectionYearDeleteView(CCEDeleteView):
    model = ElectionYear
    page_title = 'Delete Year'
    sidebar_group = ['Taxonomy',]
    success_message = 'Year Deleted Succesfully'

    def get_success_url(self):
        return reverse('browse_election_year')


class VideoFormatListView(CCESearchView):
    model = VideoFormat
    page_title = "Browse Video Format"
    sidebar_group = ['Taxonomy',]
    search_form_class = VideoFormatSimpleSearch
    columns = [
        ('Video Format Name', 'name')
    ]
    show_context_menu = True


class VideoFormatCreateView(CCECreateView):
    model = VideoFormat
    page_title = 'Create New Video Format!'
    sidebar_group = ['Taxonomy',]
    form_class = VideoFormatForm
    success_message = 'Format Created Succesfully'
    show_context_menu = True

    def get_success_url(self):
        return reverse('browse_video_format')


class VideoFormatDetailView(CCEDetailView):
    model = VideoFormat
    page_title = 'Video Format Details'
    sidebar_group = ['Taxonomy',]
    detail_fields = [
        ('Video Format Name', 'name'),
    ]
    show_context_menu = True


class VideoFormatUpdateView(CCEUpdateView):
    model = VideoFormat
    page_title = 'Edit Video Format'
    sidebar_group = ['Taxonomy',]
    show_context_menu = True
    success_message = 'Video Format Edited Succesfully'
    form_class = VideoFormatForm
    def get_success_url(self):
        return reverse('browse_video_format')


class VideoFormatDeleteView(CCEDeleteView):
    model = VideoFormat
    page_title = 'Delete Video Format'
    sidebar_group = ['Taxonomy',]
    success_message = 'Video Format Deleted Succesfully'

    def get_success_url(self):
        return reverse('browse_video_format')

