# [START gae_python38_app]
from flask import Flask
from multiprocessing import Pool
from multiprocessing import cpu_count

from custom_metric import *
import os
import random

PROJECT_ID = os.environ["PROJECT_ID"]

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

cat_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/3/38/Adorable-animal-cat-20787.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/c/c7/Tabby_cat_with_blue_eyes-3336579.jpg",
    "https://upload.wikimedia.org/wikipedia/en/0/0d/Tortoiseshell-cat.jpg"
]

dog_urls = [
    "https://upload.wikimedia.org/wikipedia/commons/1/18/Dog_Breeds.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/5/51/Lucy_the_Dog_at_The_Green%2C_Town_Square_Las_Vegas.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/4/43/Cute_dog.jpg"
]

def heavy_math(x):
    for _ in range(100000000):
        x*x

num_of_pets_requested = 0
mwriter = MetricsWriter(num_of_pets_requested)
mwriter.start()

processes = cpu_count()
pool = Pool(processes)

@app.route('/')
def hello():
    """Return some very basic HTML"""
    return f'<h1>Hello There!</h1><br/><br/><p>This is the main page</p>'

@app.route('/cat')
def cat():
    global num_of_pets_requested
    num_of_pets_requested += 1
    mwriter.update_value(num_of_pets_requested)
    cat_of_the_day = random.choice(cat_urls)
    """Return some very basic HTML"""
    return f'<h1>Hello There!</h1><br/><br/><p>Here is the cat of the day:</p><br/><img src={cat_of_the_day} width="500" height="300">'

@app.route('/dog')
def dog():
    global num_of_pets_requested
    num_of_pets_requested += 1
    mwriter.update_value(num_of_pets_requested)
    dog_of_the_day = random.choice(dog_urls)
    """Return some very basic HTML"""
    return f'<h1>Hello There!</h1><br/><br/><p>Here is the dog of the day:</p><br/><img src={dog_of_the_day} width="500" height="300">'

@app.route('/gowild')
def go_wild():
    global pool 
    pool.map(heavy_math, range(processes))
    return f'<h1>Hello There!</h1><br/><br/><p>Wow! Just finished some heavy math</p> '

@app.route('/stop')
def stop():
    global pool
    pool.terminate()
    return f'<h1>Hello There!</h1><br/><br/><p>Stopping.</p>'

if __name__ == '__main__':
    # The localhost IP and port configured here are used when running locally only. 
    # When deploying to Google App Engine, a webserver process (Gunicorn) will serve 
    # the app on regular HTTP(S) port. 
    create_metric_descriptor(PROJECT_ID)
    app.run(host='127.0.0.1', port=5012, debug=True)
# [END gae_python38_app]
