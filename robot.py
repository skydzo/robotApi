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
        proc = subprocess.Popen(['raspi-live', 'start'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()
        print('Output: ' + o.decode('ascii'))
        print('Error: ' + e.decode('ascii'))
        print('code: ' + str(proc.returncode))
    if state == "stop":
        proc = subprocess.Popen(['pkill', 'raspi-live'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        o, e = proc.communicate()
        print('Output: ' + o.decode('ascii'))
        print('Error: ' + e.decode('ascii'))
        print('code: ' + str(proc.returncode))
