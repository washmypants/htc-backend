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
PAGINATION = False
PAGINATION_LIMIT = 0
PAGINATION_DEFAULT = 0
OPTIMIZE_PAGINATION_FOR_SPEED = True
HATEOAS = False
AUTH_FIELD = True

client_schema = {
    'email': {
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
    'sub_id': {
        'type': 'string',
        'readonly': True,
        'default': ''
    },
    'password': {
        'type': 'string',
        'minlength': 6,
        'required': True
    }
}

washer_schema = {
    'email': {
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
    'running_sub_id': {
        'type': 'list',
        'default': []
    },
    'password': {
        'type': 'string',
        'minlength': 6,
        'required': True
    },
	'balance': {
		'type': 'float',
		'default': 00.00,
		'readonly': True
	}
}

subs_schema = {
	'plan_start': {
		'type': 'datetime',
		'readonly': True
	},
	'wash_total': {
		'type': 'integer',
		'default': 0,
		'readonly': True
	},
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
	},
	'taken': {
		'type': 'boolean',
		'default': False,
		'readonly': True
	},
	'address': {
		'type': 'string',
		'readonly': True
	},
	'paid': {
		'type': 'boolean',
		'default': False,
		'readonly': True
	}
}

client = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'email'
    },
    'item_title': 'client',
    'resource_methods': ['GET', 'POST'],
    'schema': client_schema,
    'cache_control': '',
    'cache_expires': 1
}

subs = {
    'item_title': 'sub',
    'resource_methods': ['GET'],
    'schema': subs_schema,
    'cache_control': '',
    'cache_expires': 1
}

washer = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'email'
    },
    'item_title': 'washer',
    'resource_methods': ['GET', 'POST'],
    'cache_control': '',
    'cache_expires': 1,
	'schema': washer_schema
}

DOMAIN = {
	'client': client,
	'subs': subs,
	'washer': washer
}
