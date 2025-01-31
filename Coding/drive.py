from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

driveL = Motor(port=Port.D, positive_direction=Direction.COUNTERCLOCKWISE)
driveR = Motor(port=Port.B, positive_direction=Direction.CLOCKWISE)
base = DriveBase(left_motor=driveL, right_motor=driveR, wheel_diameter=57.25, axle_track=99.09)
def drive():
    base.turn(1800)