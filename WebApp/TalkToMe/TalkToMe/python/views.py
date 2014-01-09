from django.shortcuts import render_to_response
from django.shortcuts import redirect

def default(request):
	return render_to_response('default.html')