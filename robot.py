from gpiozero import Robot
import os


class Robobo:

    def __init__(self):
        self.robot = Robot(left=(8, 7), right=(9, 10))

    def move(self, direction, speed):
        if direction == "forward":
            self.robot.forward()
        if direction == "backward":
            self.robot.backward()
        if direction == "left":
            self.robot.left()
        if direction == "right":
            self.robot.right()
        if direction == "stop":
            self.robot.stop()

    def camera(self, state):
        if state == "start":
            os.system('sudo /bin/sh /var/www/html/robotApi/runCamera.sh pi')
        if state == "stop":
            os.system('sudo /bin/sh /var/www/html/robotApi/stopCamera.sh')
