from flask import Flask
from flask import jsonify
import subprocess


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/<direction>/<speed>')
def move_request(direction,speed):
    return direction


@app.route('/api/camera/<state>')
def camera_request(state):
    subprocess.run(["raspi-live", state])
    return state


if __name__ == '__main__':
    app.run()
