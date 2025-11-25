#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from time import sleep

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=43, axle_track=104)
robot.settings(1000, 1000, 200, 200)
robot.straight(4700)
ev3.speaker.beep()
robot.turn(100)
ev3.speaker.beep()
robot.straight(3300)
ev3.speaker.beep()
robot.turn(50)
ev3.speaker.beep()
robot.straight(1200)
ev3.speaker.beep()
robot.turn(50)
ev3.speaker.beep()
robot.straight(5100)
ev3.speaker.beep()
sleep(1)
ev3.speaker.beep()
sleep(1)
ev3.speaker.beep()
robot.turn(-360)