from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponse
import jsonpickle

from services_impl.loginService import LoginService
from services_impl.localizationService import LocalizationService


def login(request):
    return HttpResponse(LoginService().processRequest(request))


def localization(request):
    return HttpResponse(LocalizationService().processRequest(request))