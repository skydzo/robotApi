from gpiozero import Robot
from gpiozero import DistanceSensor
import os


class Robobo:

    def __init__(self):
        self.robot = Robot(left=(7, 8), right=(10, 9))
        self.sensor = DistanceSensor(15, 18)
        self.direction = "forward"
        self.isCameraActive = 0

    def move(self, direction, speed):
        self.direction = direction
        if direction == "forward":
            dist = self.getDistance()
            if dist > 20:
                self.robot.forward()
        if direction == "backward":
            self.robot.backward()
        if direction == "left":
            self.robot.left()
        if direction == "right":
            self.robot.right()
        if direction == "stop":
            self.robot.stop()

    def getCameraStatus(self):
        return self.isCameraActive

    def camera(self, state):
        if state == "start":
            os.system('sudo /bin/sh /var/www/html/robotApi/runCamera.sh pi')
            self.isCameraActive = 1
        if state == "stop":
            os.system('sudo /bin/sh /var/www/html/robotApi/stopCamera.sh pi')
            self.isCameraActive = 0

    def getDistance(self):
        if self.direction == "forward" and round(self.sensor.distance * 100, 1) < 20:
            self.robot.stop()
            return round(self.sensor.distance * 100, 1)
        return round(self.sensor.distance * 100, 1)

