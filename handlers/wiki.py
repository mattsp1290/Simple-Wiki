from handlers.base import AppHandler
from models.user import User
from models.wiki import Wiki

class WikiHandler(AppHandler):
	def get(self, page_name):
		id = self.request.get('id')
		if id:
			wiki = Wiki.by_id(int(id))
		else:
			wiki = Wiki.by_name(page_name)
		if wiki:
			self.values['content'] = wiki.content
			self.values['page_name'] = page_name
			self.render('wiki.html')
		else:
			self.redirect('/_edit' + page_name)