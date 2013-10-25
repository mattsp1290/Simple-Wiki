from handlers.base import AppHandler
from models.user import User
from models.wiki import Wiki

class EditHandler(AppHandler):
	def get(self, page_name):
		if isinstance(self.user, User):
			self.render_form(page_name)
		else:
			self.redirect("/login")
			
	def post(self, page_name):
		content = self.request.get('content')
		if (len(content) > 0):
			wiki = Wiki(name=page_name, content=content)
			wiki.put()
			self.redirect(str(page_name))
		else:
			self.render_form(page_name, content)
			
	def render_form(self, page_name, content = ""):
		values = {}
		id = self.request.get('id')
		if id:
			wiki = Wiki.by_id(int(id))
		else:
			wiki = Wiki.by_name(page_name)
		if wiki:
			values['username'] = self.user.username
			values['page_name'] = page_name
			values['content'] = wiki.content
		self.render('edit.html', values)