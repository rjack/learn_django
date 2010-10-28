from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the poll index.")


def detail(request, poll_id):
	return HttpResponse("Poll %s" % poll_id)


def results(request, poll_id):
	return HttpResponse("Results for poll %s" % poll_id)


def vote(request, poll_id):
	return HttpResponse("Vote on poll %s" % poll_id)
