from handlers.base import AppHandler
from models.user import User
from lib import userregex
from lib import hash
import time


class SignUpHandler(AppHandler):
	def render_form(self, form_values):
		self.values = dict(self.default_form_values().items() + form_values.items())
		self.render("signup.html")
        
	def default_form_values(self):
		return {"username": '', 
                "email": ''
		}
		
	def get(self):
		self.render_form(self.default_form_values())
	
	def post(self):
		valid = True
		self.values['username'] = self.request.get('username')
		self.values['email'] = self.request.get('email')
		self.values['password'] = self.request.get('password')
		self.values['verify'] = self.request.get('verify')
		
		if (not userregex.valid_email(self.values['email']) and (len(self.values['email']) > 0)):
			valid = False
			self.values['email_error'] = "Your e-mail address is not valid"
			
		if not userregex.valid_username(self.values['username']):
			valid = False
			self.values['username_error'] = "Your username is not valid"
			
		if not userregex.valid_password(self.values['password']):
			valid = False
			self.values['password_error'] = "Your password is not valid"
			
		if not (self.values['password'] == self.values['verify']):
			valid = False
			self.values['verify_error'] = "Your passwords do not match"
			
		user_test = User.by_username(self.values['username'])
		if user_test:
			valid = False
			self.values['username_error'] = 'Your username already exists'
			
		if valid:
			salt = hash.hash(str(time.time) + "secret value")
			hashed_password = hash.hash_with_salt(self.values['password'], salt)
			user = User(username=self.values['username'], hashed_password=hashed_password, salt=salt, email=self.values['email'])
			user.put()
			self.login(user)
			self.redirect("/")
		else:
			self.render_form(self.values)
