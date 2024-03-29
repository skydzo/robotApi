from flask import Flask
from robot import Robobo


app = Flask(__name__)
robby = Robobo()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<string:direction>/<int:speed>', methods = ['GET', 'POST'])
def move_request(direction, speed):
    global robby
    robby.move(direction, speed)
    return direction


@app.route('/camera', methods = ['GET', 'POST'])
def get_camera_status_request():
    global robby
    cameraState = robby.getCameraStatus()
    return str(cameraState)


@app.route('/camera/<state>', methods = ['GET', 'POST'])
def camera_request(state):
    global robby
    robby.camera(state)
    return state


@app.route('/distance', methods = ['GET', 'POST'])
def distance():
    global robby
    distance = robby.getDistance()
    return str(distance)


if __name__ == '__main__':
    app.run()
