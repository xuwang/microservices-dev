#A Resource Owner Password Credentials Grant Service
An OAuth2 Provider which supporting the Resource Owner Password Credentials Grant as described in Section 1.3.3 of [RFC 6749][RFC-6749].

This implementation is based on [Flask-sentinel][flask-sentinel].

##Prerequisites
* registry.service, to start:

		fleetctl start /var/lib/apps/registry/units/registry.service
* mongo.service, to start:

		fleetctl start /var/lib/apps/redis/units/redis.service
* redis.service, to start:

		fleetctl start /var/lib/apps/mongo/units/mongo.service
* docker image xuwang/pyweb, to build:

		/var/lib/apps/pyweb/build.sh	

##Start Service
	fleetctl start /var/lib/apps/oauth/units/oauth.service

##User and Client Management Interface
	https://oauth.docker.local/oauth/management

##Get Access Token Example
Presume we create a user and client on [User and Client Management Interface][management-ui]:

	username: test
	password: test
	client ID: HfLOecgKKjzsaj5RTxlwEBpNhBFHGnO7LVqe00Rf
To get the access token:

	curl -X POST -d "client_id=HfLOecgKKjzsaj5RTxlwEBpNhBFHGnO7LVqe00Rf&grant_type=password&username=test&password=test" https://oauth.docker.local/oauth/token

and it returns:

	{"access_token": "ZBpGfAdzvSqVSKvhAINXRUEhaEHBJS", "token_type": "Bearer", "refresh_token": "SUZOECvyVCh0KVyT0v3iGwkdwLJYNO", "scope": ""}

To use the access token:

	curl -H "Authorization: Bearer ZBpGfAdzvSqVSKvhAINXRUEhaEHBJS" https://oauth.docker.local/endpoint
and it should retuns:

	You made it through and accessed the protected resource!

[flask-sentinel]: https://github.com/nicolaiarocci/flask-sentinel/blob/develop/README.rst
[management-ui]: https://oauth.docker.local/oauth/management
[RFC-6749]: http://tools.ietf.org/html/rfc6749#section-1.3.3