from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from taxonomy.views import TagListView, TagCreateView, TagDetailView, TagUpdateView, TagDeleteView, \
    ElectionYearListView, ElectionYearCreateView, ElectionYearDetailView, ElectionYearUpdateView, \
    ElectionYearDeleteView, VideoFormatListView, VideoFormatCreateView, VideoFormatDetailView, VideoFormatUpdateView, \
    VideoFormatDeleteView

urlpatterns = [

    url(r'^election_year/$', login_required(ElectionYearListView.as_view()), name='browse_election_year'),
    url(r'^election_year/add/', login_required(ElectionYearCreateView.as_view()), name='add_election_year'),
    url(r'^election_year/(?P<pk>\d+)/', include([
        url(r'^$', login_required(ElectionYearDetailView.as_view()), name='view_election_year'),
        url(r'^edit/$', login_required(ElectionYearUpdateView.as_view()), name='edit_election_year'),
        url(r'^delete/$', login_required(ElectionYearDeleteView.as_view()), name='delete_election_year'),
    ])),
        
    url(r'^tag/$', login_required(TagListView.as_view()), name='browse_tag'),
    url(r'^tag/add/', login_required(TagCreateView.as_view()), name='add_tag'),
    url(r'^tag/(?P<pk>\d+)/', include([
        url(r'^$', login_required(TagDetailView.as_view()), name='view_tag'),
        url(r'^edit/$', login_required(TagUpdateView.as_view()), name='edit_tag'),
        url(r'^delete/$', login_required(TagDeleteView.as_view()), name='delete_tag'),
    ])),

    url(r'^video_format/$', login_required(VideoFormatListView.as_view()), name='browse_video_format'),
    url(r'^video_format/add/', login_required(VideoFormatCreateView.as_view()), name='add_video_format'),
    url(r'^video_format/(?P<pk>\d+)/', include([
        url(r'^$', login_required(VideoFormatDetailView.as_view()), name='view_video_format'),
        url(r'^edit/$', login_required(VideoFormatUpdateView.as_view()), name='edit_video_format'),
        url(r'^delete/$', login_required(VideoFormatDeleteView.as_view()), name='delete_video_format'),
    ])),

]
