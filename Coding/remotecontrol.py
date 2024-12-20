from pybricks.parameters import Stop, Button, Port, Direction, Color
from pybricks.tools import wait
from pybricks.pupdevices import Remote, Motor
from pybricks.robotics import DriveBase
from codes import setup

'''driveL = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
driveR = Motor(Port.E, positive_direction=Direction.CLOCKWISE)
b = DriveBase(left_motor=driveL, right_motor=driveR, wheel_diameter=57.25, axle_track=99.7)
b.use_gyro(True)
'''
hub, b, auxL, auxR, colorsensor = setup()

r = Remote()
mode = 1
r.light.on(Color.GREEN)

while True:
    pressed = r.buttons.pressed()

    if Button.CENTER in pressed:
        if mode == 1:
            mode = 2
            print("Mode 2")
            r.light.on(Color.ORANGE)
        else:
            mode = 1
            print("Mode 1")
            r.light.on(Color.GREEN)

    if mode == 1:

        if Button.LEFT_PLUS in pressed:
            b.straight(10, then=Stop.NONE)

        elif Button.LEFT_MINUS in pressed:
            b.straight(-10, then=Stop.NONE)

        elif Button.RIGHT_PLUS in pressed:
            b.turn(2, then=Stop.NONE)
        
        elif Button.RIGHT_MINUS in pressed:  
            b.turn(-2, then=Stop.NONE)

        else:
            b.stop()

    '''if mode == 2:

        if Button.LEFT_PLUS in pressed:
            

        elif Button.LEFT_MINUS in pressed:

        elif Button.RIGHT_PLUS in pressed:
        
        elif Button.RIGHT_MINUS in pressed:

        else:'''

    wait(100)