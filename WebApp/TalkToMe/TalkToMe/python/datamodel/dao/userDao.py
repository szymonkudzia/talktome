import MySQLdb
from python.datamodel.dao.baseDao import BaseDao
from python.datamodel.user import User

class UserDao(BaseDao):
    TABLE_NAME = "users"
    EMAIL = "email"
    PASSWORD = "password"


    def __init__(self):
        BaseDao.__init__(self)

    def getById(self, id):
        pass

    def getByEmailAndPassword(self, email, password):
        self.openConnection()

        query = "SELECT * FROM " + self.TABLE_NAME + " WHERE " + self.EMAIL
        query += " = \'" + email + "\' AND " + self.PASSWORD + " = \'" + password  + "\'"

        result = self.executeQuery(query)

        self.closeConnection()

        if len(result) == 0:
            return None
        else:
            user = User(id = result[0]['id'], userName = result[0]['email'], password = result[0]['password'])
            return user

    def __del__(self):
        pass