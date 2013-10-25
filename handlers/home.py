from handlers.base import AppHandler
from models.user import User

class HomeHandler(AppHandler):
    def get(self):
		self.render('home.html')