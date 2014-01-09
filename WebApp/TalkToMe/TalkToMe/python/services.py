from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponse
import jsonpickle

from services_impl.loginService import LoginService
from services_impl.localizationService import LocalizationService
from services_impl.registerService import RegisterService
from services_impl.confirmService import ConfirmService
from services_impl.changePasswordService import ChangePasswordService


def login(request):
    return HttpResponse(LoginService().processRequest(request))


def localization(request):
    return HttpResponse(LocalizationService().processRequest(request))


def register(request):
    return HttpResponse(RegisterService().processRequest(request))

def confirm(request):
	return ConfirmService().processRequest(request)

def changePassword(request):
    return HttpResponse(ChangePasswordService().processRequest(request))