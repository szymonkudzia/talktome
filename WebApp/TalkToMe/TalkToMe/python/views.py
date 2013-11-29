from django.shortcuts import render_to_response

def default(request):
    return render_to_response('default.html')