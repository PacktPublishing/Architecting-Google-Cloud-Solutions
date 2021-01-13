from flask import Flask

app = Flask(__name__)

# This frontend service is stateless

@app.route('/')
def hello():
    """Return some very basic HTML"""
    return f'<h1>Hello There!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)