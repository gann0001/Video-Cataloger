from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from video.views import VideoListView, VideoCreateView, VideoDetailView, VideoUpdateView, VideoDeleteView, \
    CommentCreateView, VideoImportView

urlpatterns = [

    url(r'^import/$', login_required(VideoImportView.as_view()), name='import_videos' ),
    url(r'^$', login_required(VideoListView.as_view()), name='browse_videos' ),
    url(r'^add/$', login_required(VideoCreateView.as_view()), name='add_video'),
    url(r'^(?P<pk>\d+)/', include([
        url(r'^$', login_required(VideoDetailView.as_view()),name='view_video'),
        url(r'^edit/$', login_required(VideoUpdateView.as_view()),name='edit_video'),
        url(r'^delete/$', login_required(VideoDeleteView.as_view()),name='delete_video'),
        url(r'^comment/$', login_required(CommentCreateView.as_view()),name='add_comment'),
    ])),
]
