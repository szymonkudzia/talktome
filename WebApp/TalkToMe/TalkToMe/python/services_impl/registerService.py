import jsonpickle

import string
import random

import smtplib
from email.mime.text import MIMEText


from baseService import BaseService
from python.datamodel.user import User
from python.datamodel.dao.userDao import UserDao
from python.datamodel.dao.localizationDao import LocalizationDao

class RegisterService(BaseService):
	def processRequest(self, request):
		data = request.read()
		print 'Request data: %s' % data

		user = jsonpickle.decode(data)

		#try:
		UserDao().insertNew(user)

		user = UserDao().getByEmailAndPassword(user['email'], user['password'])
		code = self.code_generator(15) + str(user['id'])

		UserDao().insertToNotConfirmed(user, code)

		msg = self.prepareMessage(code, user['country']);
		subject = self.prepareSubject(user['country']);
		

		self.sendEmail(user['email'], subject, msg)

		#except:
			#return '{"error":true}'

		return '{}'
		
	def code_generator(self, size=10, chars=string.ascii_uppercase + string.digits):
		return ''.join([random.choice(chars) for x in range(size)])


	def prepareMessage(self, code, localization):
		link = "http://localhost:8987/service/confirm?code=" + code 

		msg = self.getTranslation('confirmationEmail', localization)

		if len(msg) <= 1:
			msg = self.getTranslation('confirmationEmail', 'en-us')

		return msg % link


	def prepareSubject(self, localization):
		subject = self.getTranslation('confirmationEmailSubject', localization)

		if len(subject) <= 1:
			subject = self.getTranslation('confirmationEmailSubject', 'en-us');

		return subject


	def getTranslation(self, field, localization):
		return  LocalizationDao().getTranslationFor([field], localization)[field]


	def sendEmail(self, email, subject, msg):
		_email = MIMEText(msg, _charset="UTF-8")
		_email['Subject'] = subject
		_email['From'] = 'talktome.student.project@talktome.com'
		_email['To'] = email

		s = smtplib.SMTP("smtp.gmail.com", 587)
		s.ehlo()
		s.starttls()
		s.login("talktome.student.project", "jakieshaslo")
		s.sendmail('talktome.student.project@talktome.com', [email], _email.as_string())
		s.quit()