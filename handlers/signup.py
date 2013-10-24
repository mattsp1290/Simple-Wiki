from handlers.base import AppHandler
from models.user import User
from lib import userregex
from lib import hash
import time


class SignUpHandler(AppHandler):
	def render_form(self, form_values):
		values = dict(self.default_form_values().items() + form_values.items())
		self.render("signup.html", values)
        
	def default_form_values(self):
		return {"username": '', 
                "email": ''
		}
		
	def get(self):
		self.render_form(self.default_form_values())
	
	def post(self):
		valid = True
		values = {}
		values['username'] = self.request.get('username')
		values['email'] = self.request.get('email')
		values['password'] = self.request.get('password')
		values['verify'] = self.request.get('verify')
		
		if (not userregex.valid_email(values['email']) and (len(values['email']) > 0)):
			valid = False
			values['email_error'] = "Your e-mail address is not valid"
			
		if not userregex.valid_username(values['username']):
			valid = False
			values['username_error'] = "Your username is not valid"
			
		if not userregex.valid_password(values['password']):
			valid = False
			values['password_error'] = "Your password is not valid"
			
		if not (values['password'] == values['verify']):
			valid = False
			values['verify_error'] = "Your passwords do not match"
			
		user_test = User.by_username(values['username'])
		if user_test:
			valid = False
			values['username_error'] = 'Your username already exists'
			
		if valid:
			salt = hash.hash(str(time.time) + "secret value")
			hashed_password = hash.hash_with_salt(values['password'], salt)
			user = User(username=values['username'], hashed_password=hashed_password, salt=salt, email=values['email'])
			user.put()
			self.login(user)
			self.redirect("/")
		else:
			self.render_form(values)
