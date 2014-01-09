import MySQLdb
import jsonpickle
from datetime import datetime
from python.datamodel.dao.baseDao import BaseDao
from python.datamodel.user import User

class UserDao(BaseDao):
	TABLE_NAME = "users"
	EMAIL = "email"
	PASSWORD = "password"


	def __init__(self):
		BaseDao.__init__(self)

	def getById(self, id):
		self.openConnection()

		query = "SELECT * FROM %s WHERE %s  = %d"  % (self.TABLE_NAME, 'id', id)

		result = self.executeQuery(query)

		self.closeConnection()

		if len(result) == 0:
			return None
		else:
			user = result[0]
			return user


	def getByEmail(self, email):
		self.openConnection()

		query = "SELECT * FROM %s WHERE %s  = '%s'"  % (self.TABLE_NAME, self.EMAIL, email)

		result = self.executeQuery(query)

		self.closeConnection()

		if len(result) == 0:
			return None
		else:
			user = result[0]
			return user



	def getByEmailAndPassword(self, email, password):
		self.openConnection()

		query = "SELECT * FROM " + self.TABLE_NAME + " WHERE " + self.EMAIL
		query += " = \'" + email + "\' AND " + self.PASSWORD + " = \'" + password  + "\'"

		result = self.executeQuery(query)

		self.closeConnection()

		if len(result) == 0:
			return None
		else:
			user = result[0]
			return user

	def isConfirmed(self, user):
		response = 1;

		self.openConnection()

		query = "SELECT * FROM users_not_confirmed WHERE userId = '%s'" % (user['id']) 

		result = self.executeQuery(query)

		if len(result) > 0:
			response = 0			

		self.closeConnection();


		return response;


	def insertNew(self, user):
		self.openConnection()

		query =  "INSERT INTO `users` (`firstName`, `lastName`, `email`, `password`,`country`,`birthdate`) VALUES"
		query += "('" + user['firstName'] + "','" + user['lastName'] + "', '" + user['email'] + "','" 
		query += user['password'] + "','" + user['country'] + "','" + user['birthdate'] + "')"

		self.execute(query);

		self.closeConnection()



	def insertToNotConfirmed(self, user, code):
		self.openConnection()

		query = "INSERT INTO users_not_confirmed (userId, inserted_date, code) VALUES(" 
		query += str(user['id']) + "," + "'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "'" + ",'" + code + "')"

		self.execute(query)

		self.closeConnection()


	def notConfirmed(self, code):
		self.openConnection()

		query = "SELECT * FROM users_not_confirmed WHERE code = '" + code + "';"

		result = self.executeQuery(query)

		
		self.closeConnection()

		if len(result) > 0:
			return 1
		return 0


	def confirm(self, code):
		self.openConnection()

		query = "DELETE FROM users_not_confirmed WHERE code = '" + code + "';"

		self.execute(query)

		self.closeConnection()


	def update(self, user):
		self.openConnection()

		try:
			query = "UPDATE users SET email='%s', password='%s', country='%s',"
			query += " birthdate='%s', firstName='%s', lastName='%s' WHERE id=%d" 
			query %= (user['email'], user['password'], user['country'], user['birthdate'], user['firstName'], user['lastName'], user['id'])

			self.execute(query)
		except:
			print 'Cannot update user: %s' % jsonpickle.encode(user)
			raise

		self.closeConnection()

	def __del__(self):
		pass