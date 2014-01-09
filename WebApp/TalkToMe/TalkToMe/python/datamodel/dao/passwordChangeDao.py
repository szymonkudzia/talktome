import MySQLdb
from datetime import datetime
from python.datamodel.dao.baseDao import BaseDao

class PasswordChangeDao(BaseDao):
	def __init__(self):
		BaseDao.__init__(self)



	def insert(self, user, code):
		self.openConnection()

		self.execute("INSERT INTO talk_to_me.password_change VALUES (%d, '%s', '%s')" % (user['id'], code, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

		self.closeConnection()



	def getUserIdByCode(self, code):
		self.openConnection();

		result = None
		try:
			result = self.executeQuery("SELECT * FROM talk_to_me.password_change WHERE code = '%s'" % code)
		except:
			print 'Could not fetch userId form  password_change where code = "%s"' % code

		self.closeConnection();

		if len(result) > 0:
			return result[0]['userId']
		return -1



	def deleteCode(self, code):
		self.openConnection()

		self.execute("DELETE FROM talk_to_me.password_change WHERE code = '%s'" % code)

		self.closeConnection()
		


