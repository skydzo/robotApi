from flask import Flask
import robot


app = Flask(__name__)

robby = robot()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<string:direction>/<int:speed>', methods = ['GET', 'POST'])
def move_request(direction, speed):
    global robot
    robby.move(direction, speed)
    return direction


@app.route('/camera/<state>', methods = ['GET', 'POST'])
def camera_request(state):
    global robot
    robby.camera(state)
    return state


if __name__ == '__main__':
    app.run()
