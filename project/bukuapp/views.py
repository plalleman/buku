from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

from django.http import HttpResponse

def index(request):
	context = RequestContext(request)
	context_dict = {}
	return render_to_response('bukuapp/index.html', context_dict, context)
