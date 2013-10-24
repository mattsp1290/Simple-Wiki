import os
import re
import jinja2
import webapp2

# Set useful fields
root_dir = os.path.dirname(__file__)
template_dir = os.path.join(root_dir, 'templates')
jinja_environment = jinja2.Environment(autoescape=True,
        loader=jinja2.FileSystemLoader(template_dir))


app = webapp2.WSGIApplication([
    (r'/', 'handlers.home.HomeHandler'),
	(r'/signup', 'handlers.signup.SignUpHandler'),
	(r'/login', 'handlers.login.LoginHandler'),
	(r'/logout', 'handlers.logout.LogoutHandler')
], debug=True)
