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
        subprocess.call(["raspi-live", state])
    if state == "stop":
        subprocess.call(["raspi-live", state])
