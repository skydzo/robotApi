from gpiozero import Robot
import subprocess


robot = Robot(left=(8, 7), right=(9, 10))


def move(direction,speed):
    if direction == "forward":
        robot.forward(speed)
    if direction == "backward":
        robot.backward(speed)
    if direction == "left":
        robot.left(speed)
    if direction == "right":
        robot.right(speed)
    if direction == "stop":
        robot.stop()

def camera(state):
    if state == "start":
        subprocess.run(["raspi-live", state])
    if state == "stop":
        subprocess.run(["raspi-live", state])
