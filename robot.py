from gpiozero import Robot
import subprocess


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
        subprocess.check_call(["raspi-live", "start"], shell=True)
    if state == "stop":
        subprocess.check_call(["raspi-live", "stop"], shell=True)
