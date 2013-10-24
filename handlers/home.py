from handlers.base import AppHandler
from models.user import User

class HomeHandler(AppHandler):
    def get(self):
		values = {}
		if self.user:
			values['username'] = self.user.username
		self.render('home.html', values)