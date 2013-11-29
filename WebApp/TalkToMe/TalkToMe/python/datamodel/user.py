class User:
    def __init__(self, id = None, userName = None, password = None):
        self.id = id;
        self.userName = userName;
        self.password = password;


    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setUserName(self, name):
        self.userName = name

    def getUserName(self):
        return self.userName

    def setPassword(self, password):
        self.password = password

    def getPassword(self):
        return self.password