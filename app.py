from flask import Flask
import robot


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<direction>/<speed>', methods = ['GET', 'POST'])
def move_request(direction, speed):
    robot.move(direction, speed)
    return direction


@app.route('/camera/<state>', methods = ['GET', 'POST'])
def camera_request(state):
    robot.camera(state)
    return state


if __name__ == '__main__':
    app.run()
