import os

if os.environ.get('DEV'):
	MONGO_URI = 'mongodb://localhost:27017/test'
	DEBUG = True
else:
	# production
	MONGO_URI = 'mongodb://localhost:27017/main'


X_HEADERS = ['Content-Type', 'Authorization', 'X-HTTP-Method-Override', 'If-Match', 'X-Requested-With']
URL_PREFIX = 'api'
X_DOMAINS = '*'
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PUT']
ALLOWED_FILTERS = []
PAGINATION = False
PAGINATION_LIMIT = 0
PAGINATION_DEFAULT = 0
OPTIMIZE_PAGINATION_FOR_SPEED = True
HATEOAS = False
AUTH_FIELD = True

client_schema = {
    'email': {
        'email': True,
        'type': 'string',
        'minlength': 3,
        'unique': True,
        'required': True
    },
    'full_name': {
        'type': 'string',
        'required': True
    },
    'address': {
        'type': 'string',
        'required': True
    },
    '''
    	active subscription id (reference)
    '''
    'sub_id': {
        'type': 'string',
        'required': True
    },
    'password': {
        'type': 'string',
        'minlength': 6,
        'required': True
    }
}

washer_schema = {
    'email': {
        'email': True,
        'type': 'string',
        'minlength': 3,
        'unique': True,
        'required': True
    },
    'full_name': {
        'type': 'string',
        'required': True
    },
    'address': {
        'type': 'string',
        'required': True
    },
    '''
    	running subscription ids (reference)
    '''
    'running_sub_id': {
        'type': 'list',
        'required': True
    },
    'password': {
        'type': 'string',
        'minlength': 6,
        'required': True
    }
}

subs_schema = {
	'plan_start': {
		'type': 'datetime',
		'readonly': True
	},
	'plan_end': {
		'type': 'datetime',
		'readonly': True
	},
	'wash_total': {
		'type': 'integer',
		'default': 0,
		'readonly': True
	},
	'''
		price for 1 wash
	'''
	'wash_price': {
		'type': 'float',
		'default': 25.00,
		'readonly': True
	},
	'wash_weekly': {
		'type': 'integer',
		'default': 0,
		'readonly': True
	},
	'wash_done': {
		'type': 'integer',
		'default': 0,
		'readonly': True
	}
}

client = {
    'item_title': 'client',
    'resource_methods': ['POST'],
    'schema': client_schema,
    'cache_control': 'max-age=5,must-revalidate',
    'cache_expires': 5
}

subs = {
    'item_title': 'sub',
    'resource_methods': [],
    'schema': subs_schema,
    'cache_control': 'max-age=5,must-revalidate',
    'cache_expires': 5
}

washer = {
    'item_title': 'sub',
    'resource_methods': ['POST'],
    'cache_control': 'max-age=5,must-revalidate',
    'cache_expires': 5,
	'schema': washer_schema
}

DOMAIN = {
	'client': client,
	'subs': subs,
	'washer': washer
}
