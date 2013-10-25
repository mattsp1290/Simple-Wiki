from handlers.base import AppHandler
from models.user import User

class LoginHandler(AppHandler):
	def render_form(self, login_error=False):
		self.values['login_error'] = login_error
		self.render("login.html")
	
	def get(self):
		self.render_form()
		
	def post(self):
		redirect = False
		username = self.request.get('username')
		password = self.request.get('password')
		
		if (User.login(username, password)):
			user = User.by_username(username)
			self.login(user)
			self.redirect("/")
		else:
			self.render_form(login_error=True)
