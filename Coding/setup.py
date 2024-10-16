from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase

def setup():
    #Setup the hub with the top side (with the USB) as the X axis and the front side (with the buttons) as the Y axis
    hub = PrimeHub(top_side=Axis.Y, front_side=-Axis.Y)

    #Set the stop button to the bluetooth button 
    #This will stop the ENTIRE program, including the main code which includes the menu, but this can be fixed by pressing the centre button when the square shown on the Prime Hub display
    hub.system.set_stop_button(Button.BLUETOOTH)

    #Swap Clockwise and Counterclockwise here if robot is driving backward when it should be driving forward
    driveL = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
    driveR = Motor(Port.E, positive_direction=Direction.CLOCKWISE)

    #Setup auxiliary motors and colour sensor
    auxL = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
    auxR = Motor(Port.F, positive_direction=Direction.CLOCKWISE)
    auxCS = ColorSensor(Port.D)

    #Setup the DriveBase with the left motor as driveL, the right motor as driveR, the wheel diameter as 57.25mm and the axle track (width between the middle of the wheels) as 99.09mm
    base = DriveBase(left_motor=driveL, right_motor=driveR, wheel_diameter=57.25, axle_track=99.09).use_gyro(True)

    #Return the hub, left aux motor, right aux motor, colour sensor and DriveBase in that order so it can be referenced and used in the main code as well as other auxiliary codes to ensure every code uses the same parameters
    return hub, auxL, auxR, auxCS, base