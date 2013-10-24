from handlers.base import AppHandler
from models.user import User
from models.wiki import Wiki

class WikiHandler(AppHandler):
	def get(self, page_name):
		values = {}
		values['username'] = self.user.username
		wiki = Wiki.by_name(page_name)
		if wiki:
			values['content'] = wiki.content
			self.render('wiki.html', values)
		else:
			self.redirect('/_edit' + page_name)