# [START gae_python38_app]
from flask import Flask
import os

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

# This is set in app.yaml
custom_env_var = os.environ['MY_CUSTOM_ENV_VAR']

app_file = open('app.yaml', 'r')
app_content = app_file.read().replace('\n','<br/>').replace('  ',"&nbsp;&nbsp;&nbsp;&nbsp;")
app_file.close()

@app.route('/')
def hello():
    """Return some very basic HTML"""
    return f'<h1>Hello There!</h1><p><img src={custom_env_var} width="500" height="300"></p><p>Here is the content of my app.yaml: <br/><br/><i>{app_content}</i>'


if __name__ == '__main__':
    # The localhost IP and port configured here are used when running locally only. 
    # When deploying to Google App Engine, a webserver process (Gunicorn) will serve 
    # the app on regular HTTP(S) port. 
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
