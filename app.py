from eve import Eve
from eve.auth import BasicAuth
from flask import current_app, request, Response, jsonify, make_response, abort
import os, json

DEFAULT_PASSW = "hack-the-city-2017"

class MyBasicAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
    	print(method, resource, request.path)
    	if resource is not None:
    		# allow signup/login
	    	if (method == "POST"):
	    		print("signup/login")
	    		return True
        return password == DEFAULT_PASSW

def authenticate(self):
    resp = Response(None, 401)
    abort(401, description='Please provide proper credentials', response=resp)

# override auth fn
MyBasicAuth.authenticate = authenticate

app = Eve(auth=MyBasicAuth)

def CORS_reply ():
	resp = make_response('')
	resp.headers.add('Access-Control-Allow-Origin', '*')
	resp.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
	return resp

def reply (obj):
	resp = make_response(jsonify(obj))
	resp.headers.add('Access-Control-Allow-Origin', '*')
	resp.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
	return resp

@app.route('/api/login', methods=["OPTIONS", "POST"])
def login():
	if request.method == 'OPTIONS':
		return CORS_reply()
	reply_auth = {"success": False}
	content = request.get_json(silent=True)
	email = content["email"]
	password = DEFAULT_PASSW
	client = current_app.data.driver.db['client']
	client_match = client.find_one({"email": email})
	# TODO washer before client
	if client_match is None:
		washer = current_app.data.driver.db['washer']
		washer_match = washer.find_one({"email": email})
		if washer_match is not None:
			reply_auth["success"] = True
			reply_auth["type"] = "washer"
			reply_auth["full_name"] = washer_match["full_name"]
	else:
		reply_auth["success"] = True
		reply_auth["type"] = "client"
		reply_auth["full_name"] = client_match["full_name"]
	
	return reply(reply_auth)

def before_client_insert(resource):
	print("client reg")
	resource = resource[0]
	washer = current_app.data.driver.db['washer']
	# check if washer collection contains the email
	washer_match = washer.find_one({'email': resource["email"]})
	if washer_match is not None:
		raise Exception('email not unique')
	resource["password"] = DEFAULT_PASSW
	resource = [resource]

def before_washer_insert(resource):
	print("washer reg")
	resource = resource[0]
	client = current_app.data.driver.db['client']
	# check if client collection contains the email
	client_match = client.find_one({'email': resource["email"]})
	if washer_match is not None:
		raise Exception('email not unique')
	resource["password"] = DEFAULT_PASSW
	resource = [resource]

app.on_insert_client += before_client_insert
app.on_insert_washer += before_washer_insert

if __name__ == '__main__':
    app.run()
