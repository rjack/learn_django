from django.template import Context, loader
from polls.models import Poll
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404



def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('polls/index.html')
	c = Context({
		'latest_poll_list': latest_poll_list
	})
	return HttpResponse(t.render(c))



def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render_to_response("polls/detail.html", {
		'poll': poll
	})


def results(request, poll_id):
	return HttpResponse("Results for poll %s" % poll_id)


def vote(request, poll_id):
	return HttpResponse("Vote on poll %s" % poll_id)
