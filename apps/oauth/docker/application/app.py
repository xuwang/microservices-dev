from flask import Flask
from flask.ext.sentinel import ResourceOwnerPasswordCredentials, oauth
from flask.ext.sentinel.core import redis
from redis.connection import ConnectionPool

app = Flask(__name__)
app.config.from_object('setup')

# workaround on a redis connection bug in flask-sentinel v0.0.2
redis.connection_pool=ConnectionPool.from_url(app.config['SENTINEL_REDIS_URL'])

ResourceOwnerPasswordCredentials(app)

@app.route('/endpoint')
@oauth.require_oauth()
def restricted_access():
    return "You made it through and accessed the protected resource!"

if __name__ == '__main__':
    app.run(ssl_context='adhoc')