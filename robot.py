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
        subprocess.Popen(['raspi-live', 'start'])
        subprocess.Popen(['ffmpeg', '-re', '-i', 'pipe:0', '-y', '-an', '-vcodec', 'copy', '-f', 'hls', '-hls_time', '2', '-hls_list_size', '10', '-hls_delete_threshold', '10', '-hls_flags', 'split_by_time+delete_segments+second_level_segment_index', '-strftime', '1', '-hls_segment_filename', '/home/pi/camera/%s-%%d.m4s', '-hls_segment_type', 'fmp4', '/home/pi/camera/livestream.m3u8'])
    if state == "stop":
        subprocess.Popen(['raspi-live', 'stop'])

