import MySQLdb
from python.datamodel.dao.baseDao import BaseDao
from python.datamodel.localization import Localization

class LocalizationDao(BaseDao):
	def __init__(self):
		BaseDao.__init__(self)

	def getById(self, id):
		pass

	def getByLocalization(self, localization):
		self.openConnection()


		local = Localization()

		for key in local.data.keys():
			local.data[key] = self._selectValue(key, localization)

		self.closeConnection()

		return local


	def _selectValue(self, fieldName, localization):
		query = "SELECT value FROM localization WHERE localization"
		query += " = \'" + localization + "\' AND fieldName = \'" + fieldName  + "\'"

		result = self.executeQuery(query)

		if result:
			return result[0]["value"]

		return ""



	def getTranslationFor(self, fieldNames, localization):
		translations = {}

		self.openConnection()

		for fieldName in fieldNames:
			translations[fieldName] = self._selectValue(fieldName, localization)

		self.closeConnection()


		return translations



	def getLanguages(self):
		self.openConnection()

		query = "SELECT * FROM localization WHERE fieldName = 'languageName'"
		result = self.executeQuery(query)

		self.closeConnection()

		languages = []

		for r in result:
			languages.append({"code" : r["localization"], "name": r["value"]})

		return languages


