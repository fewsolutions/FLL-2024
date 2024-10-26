from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

driveL = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
driveR = Motor(Port.E, positive_direction=Direction.CLOCKWISE)
base = DriveBase(left_motor=driveL, right_motor=driveR, wheel_diameter=57.25, axle_track=99.09)
base.use_gyro(True)

base.straight(500)