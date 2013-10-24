from handlers.base import AppHandler


class LogoutHandler(AppHandler):
	def get(self):
		self.logout()
		self.redirect("/signup")
		
