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
app_file = open('app.yaml', 'r')
app_content = app_file.read()
app_file.close()

@app.route('/')
def hello():
    """Return some very basic HTML"""
    return f'<h1>Hello There!</h1><br/><br/><p>My instance id is <b>{instance}</b>.</p><br/><p>I am running on <b>{env}</b> environment. My Runtime is <b>{runtime}</b>.</p><p>Here is the content of my app.yaml: <br/><br/><i>{app_content}</i>'


if __name__ == '__main__':
    # The localhost IP and port configured here are used when running locally only. 
    # When deploying to Google App Engine, a webserver process (Gunicorn) will serve 
    # the app on regular HTTP(S) port. 
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
