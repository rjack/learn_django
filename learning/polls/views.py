from django.template import Context, RequestContext, loader
from polls.models import Poll, Choice
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse



def index(request):
	latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('polls/index.html')
	c = Context({
		'latest_poll_list': latest_poll_list
	})
	return HttpResponse(t.render(c))



def detail(request, poll_id, voted=False):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render_to_response("polls/detail.html", {
		'poll': poll,
		'voted': voted,
	}, context_instance=RequestContext(request))


def results(request, poll_id):
	return detail(request, poll_id, True)


def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form
		return render_to_response('polls/detail.html', {
			'poll': p,
			'error_message': "You did't select a choice!"
		}, context_instance = RequestContext(request))
	else:
		# All went good: increment votes, save changes and redirect to results
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls.views.results",
			args=(p.id,)))
