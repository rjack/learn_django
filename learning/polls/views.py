from django.template import Context, RequestContext, loader
from polls.models import Poll, Choice
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse


def vote(request, object_id):
	p = get_object_or_404(Poll, pk=object_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the poll voting form
		return render_to_response('polls/poll_detail.html', {
			'object': p,
			'error_message': "You did't select a choice!"
		}, context_instance = RequestContext(request))
	else:
		# All went good: increment votes, save changes and redirect to results
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse("poll_results", args=(p.id,)))
