# [START gae_python38_app]
from flask import Flask
import os

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

# Fetch some environment variables set by App Engine
runtime = os.environ['GAE_RUNTIME']
env = os.environ['GAE_ENV']
instance = os.environ['GAE_INSTANCE']

@app.route('/')
def hello():
    """Return some very basic HTML"""
    return f'<h>Hello There!</h><br/><br/><p>My instance id is <b>{instance}</b> and I am running on <b>{env}</b> environment. My Runtime is <b>{runtime}</b></p>'


if __name__ == '__main__':
    # The localhost IP and port configured here are used when running locally only. 
    # When deploying to Google App Engine, a webserver process (Gunicorn) will serve 
    # the app on regular HTTP(S) port. 
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
