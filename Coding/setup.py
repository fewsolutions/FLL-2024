from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

def setup():
    hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
    hub.system.set_stop_button(Button.BLUETOOTH)

    driveL = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
    driveR = Motor(Port.E, positive_direction=Direction.CLOCKWISE)

    auxL = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
    auxR = Motor(Port.F, positive_direction=Direction.CLOCKWISE)

    auxCS = ColorSensor(Port.D)

    base = DriveBase(left_motor=driveL, right_motor=driveR, wheel_diameter=57.25, axle_track=99.09)
    base.use_gyro(True)

    return hub, auxL, auxR, auxCS, base
