import os

if os.environ.get('DEV'):
	MONGO_URI = 'mongodb://localhost:27017/test'
	DEBUG = True
else:
	# production
	MONGO_URI = 'mongodb://localhost:27017/main'


X_DOMAINS = '*'
RESOURCE_METHODS = ['GET', 'POST']



DOMAIN = {

}
