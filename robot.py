from gpiozero import Robot
import subprocess
import os


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
        os.system('raspi-live start')
        subprocess.call(['raspi-live', 'start'], shell=True)
    if state == "stop":
        os.system('raspi-live stop')
        subprocess.call(['raspi-live', 'stop'], shell=True)


def camera2(state):
    process = subprocess.Popen(['raspi-live', 'start'], shell=True, stdout=subprocess.PIPE)
    process.wait()
    print process.returncode
