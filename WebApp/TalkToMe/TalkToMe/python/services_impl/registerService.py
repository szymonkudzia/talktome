import jsonpickle
from baseService import BaseService


class registerService(BaseService):
	def processRequest(self, request):
		data = request.read()
		print 'Request data: %s' % data

		registerForm = jsonpickle.decode(data)


		