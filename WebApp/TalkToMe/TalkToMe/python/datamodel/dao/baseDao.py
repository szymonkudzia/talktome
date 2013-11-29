import MySQLdb
from python.settings import DATABASES

class BaseDao:
    def __init__(self):
        self.host = DATABASES['default']['HOST']
        self.port = int(DATABASES['default']['PORT'])
        self.db = DATABASES['default']['NAME']
        self.userName = DATABASES['default']['USER']
        self.password = DATABASES['default']['PASSWORD']



    def openConnection(self):
        self.connection = MySQLdb.connect(host = self.host, port = self.port, 
                                          user = self.userName, passwd = self.password, 
                                          db = self.db, charset='utf8')


    def closeConnection(self):
        self.connection.close()


    def executeQuery(self, query):
        cursor = self.getConnection().cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)

        return cursor.fetchall()


    def getConnection(self):
        return self.connection;