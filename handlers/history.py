from handlers.base import AppHandler
from models.user import User
from models.wiki import Wiki

class HistoryHandler(AppHandler):
	def get(self, page_name):
		self.values['page_name'] = page_name
		wikis = Wiki.all().filter('name =', page_name).order('-created')
		wikis_list = []
		for wiki in wikis:
			wikis_list.append({'created': wiki.created, 'content': (self.cap(wiki.content, 100)), 'id': (wiki.key().id())})
		if wikis:
			self.values['wikis'] = wikis_list
			self.render('history.html')
		else:
			self.redirect('/_edit' + page_name)
			
	def cap(self, string, length):
		return string if len(string)<=length else string[0:length-3]+'...'