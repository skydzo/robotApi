from flask import Flask
from gpiozero import Robot
import os
# import robot


app = Flask(__name__)


robot = Robot(left=(8, 7), right=(9, 10))


def move(direction, speed):
    if direction == "forward":
        robot.forward()
    if direction == "backward":
        robot.backward()
    if direction == "left":
        robot.left()
    if direction == "right":
        robot.right()
    if direction == "stop":
        robot.stop()


def camera(state):
    if state == "start":
        os.system('sudo /bin/sh /var/www/html/robotApi/runCamera.sh pi')
    if state == "stop":
        os.system('sudo /bin/sh /var/www/html/robotApi/stopCamera.sh')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/<string:direction>/<int:speed>', methods = ['GET', 'POST'])
def move_request(direction, speed):
    move(direction, speed)
    return direction


@app.route('/camera/<state>', methods = ['GET', 'POST'])
def camera_request(state):
    camera(state)
    return state


if __name__ == '__main__':
    app.run()
