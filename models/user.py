from google.appengine.ext import db
from lib import hash

class User(db.Model):
	username = db.StringProperty(required=True)
	hashed_password = db.StringProperty(required=True)
	salt = db.StringProperty(required=True)
	email = db.StringProperty(required=False)
	created = db.DateTimeProperty(auto_now_add=True)
	
	@classmethod
	def by_id(cls, user_id):
		return cls.get_by_id(user_id)
		
	@classmethod
	def by_username(cls, name):
		return cls.all().filter('username =', name).get()
		
	@classmethod
	def login(cls, name, pw):
		user = cls.by_username(name)
		if user and (user.hashed_password == hash.hash_with_salt(pw, user.salt)):
			return user