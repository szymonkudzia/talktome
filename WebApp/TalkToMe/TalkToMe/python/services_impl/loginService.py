import jsonpickle
from baseService import BaseService

from python.datamodel.dao.userDao import UserDao

class LoginService(BaseService):
	def __init__(self):
		pass

	def processRequest(self, request):
		data = request.read()
		print 'Request data: %s' % data

		loginForm = jsonpickle.decode(data)

		if 'email' not in loginForm.keys() or 'password' not in loginForm.keys():
			return '{"null": "true"}'

		user = UserDao().getByEmailAndPassword(loginForm['email'], loginForm['password'])

		if user:
			if UserDao().isConfirmed(user):
				user['password'] = None
				return jsonpickle.encode(user)

		return '{"null": "true"}'