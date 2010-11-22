from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list, object_detail
from learning.polls.models import Poll
from learning.polls.views import vote


# This is lazy, so it doesn't hit the database until needed inside a view
info_dict = {
	"queryset": Poll.objects.all(),
}


urlpatterns = patterns('',
	url(r'^$', object_list, info_dict, name="poll_list"),
	url(r'^(?P<object_id>\d+)/$', object_detail, info_dict, name="poll_detail"),
	url(r'^(?P<object_id>\d+)/results/$',
		object_detail,
		dict(info_dict, template_name="polls/results.html"),
		name="poll_results"),
	url(r'^(?P<object_id>\d+)/vote/$', vote, name="poll_vote"),
)
