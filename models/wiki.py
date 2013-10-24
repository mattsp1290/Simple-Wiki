from google.appengine.ext import db

class Wiki(db.Model):
	name = db.StringProperty(required=True)
	content = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)
	
	@classmethod
	def by_name(cls, page_name):
		return cls.all().filter('name =', page_name).get()