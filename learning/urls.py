from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('polls.views',
	(r'^polls/$', 'index'),
	(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
	(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
	(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
	(r'^admin/', include(admin.site.urls)),
)
