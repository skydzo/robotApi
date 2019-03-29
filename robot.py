from gpiozero import Robot
from gpiozero import DistanceSensor
import os


class Robobo:

    def __init__(self):
        self.robot = Robot(left=(8, 7), right=(9, 10))
        self.sensor = DistanceSensor(15, 18)

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

    def getDistance(self):
        if self.sensor.distance*100 < 4:
            self.robot.stop()
            return self.sensor.distance * 100
        return self.sensor.distance*100

