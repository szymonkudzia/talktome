import jsonpickle
from django.shortcuts import redirect

from baseService import BaseService
from python.datamodel.dao.userDao import UserDao

class ConfirmService(BaseService):
	def __init__(self):
		pass

	def processRequest(self, request):
		code = request.GET['code']

		print 'Request data: %s' % code

		if not UserDao().notConfirmed(code):
			return redirect('/#/login/false')

		UserDao().confirm(code)
		return redirect('/#/login/true') # confirmed