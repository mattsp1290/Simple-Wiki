import jinja2
import webapp2

from routes import template_dir
from models.user import User
from lib import hash

# Initialize the jinja2 environment
jinja_environment = jinja2.Environment(autoescape=True,
        loader=jinja2.FileSystemLoader(template_dir))

class AppHandler(webapp2.RequestHandler):
    """Base handler, encapsulating jinja2 functions."""
    def read_secure_cookie(self, name):
        cookie_value = self.request.cookies.get(name)
        return cookie_value and hash.check_secure_value(cookie_value)

    def set_secure_cookie(self, name, value):
	    cookie_value = hash.make_secure_value(value)
	    self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_value))

    def __init__(self, request=None, response=None):
        """Initialize the handler."""
        super(AppHandler, self).__init__(request, response)
        self.jinja = jinja_environment

    def write(self, string):
        """Write an arbitrary string to the response stream."""
        self.response.out.write(string)

    def render_str(self, template_name, values=None, **kwargs):
        """Render a jinja2 template and return it as a string."""
        template = self.jinja.get_template(template_name)
        return template.render(values or kwargs)

    def render(self, template_name, values=None, **kwargs):
        """Render a jinja2 template using a dictionary or keyword arguments."""
        self.write(self.render_str(template_name, values or kwargs))

    def redirect_to(self, name, *args, **kwargs):
        """Redirect to a URI that corresponds to a route name."""
        self.redirect(self.uri_for(name, *args, **kwargs))
		
    def login(self, user):
	    self.set_secure_cookie('user_id', str(user.key().id()))
	
    def logout(self):
        self.response.headers.add_header("Set-Cookie", str("user_id=""; Path=/"))
		
	def get_username(self):
		if isinstance(self.user, User):
			return self.user.username
		else:
			return None
        
    def initialize(self, *a, **kw):
		webapp2.RequestHandler.initialize(self, *a, **kw)
		user_id = self.read_secure_cookie('user_id')
		self.user = user_id and User.by_id(int(user_id))
		
