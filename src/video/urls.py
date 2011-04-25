from django.conf.urls.defaults import *
from video.views import *

urlpatterns = patterns('',
	(r'^videos/', 'video.views.galeria'),
	(r'^video/(?P<video_id>\d+)/$', 'video.views.galeria_video'),
)
