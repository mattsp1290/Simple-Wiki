import hashlib
import hmac

salt = 'eabd522910ccdd77aef079feff0c7bb6486f6ab207ae6d3ed9e671208c92ab0f'

def make_secure_value(value):
	return '%s|%s' % (value, hmac.new(salt, value).hexdigest())
	
def check_secure_value(secure_value):
	value = secure_value.split('|')[0]
	if secure_value == make_secure_value(value):
		return value

def hash(value):
	return hashlib.sha256(value).hexdigest()
	
def hash_with_salt(value, salt):
	return hmac.new(str(salt), str(value), digestmod=hashlib.sha256).hexdigest()
