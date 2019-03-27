from gpiozero import Robot
import os


class robot:

    def __init__(self):
        self.robot = Robot(left=(8, 7), right=(9, 10))
        # web variables
        self.vitesseWeb = 500
        # self.virage = -10
        self.stopLooping = False

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


if __name__ == '__main__':
    robot = Robot()
