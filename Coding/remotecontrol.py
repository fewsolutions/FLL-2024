from pybricks.parameters import Stop, Button, Port, Direction, Color
from pybricks.tools import wait
from pybricks.pupdevices import Remote, Motor
from pybricks.robotics import DriveBase
from codes import setup

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

    if Button.LEFT in pressed:
        print(f"{b.distance()} mm")

    if Button.RIGHT in pressed:
        print(f"{b.angle()} degrees")

    if Button.LEFT in pressed and Button.RIGHT in pressed:
        print("Reset")
        b.reset()

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

    if mode == 2:

        if Button.LEFT_PLUS in pressed:
            auxL.run(200)

        elif Button.LEFT_MINUS in pressed:
            auxL.run(-200)

        else:
            auxL.stop()

        if Button.RIGHT_PLUS in pressed:
            auxR.run(200)
        
        elif Button.RIGHT_MINUS in pressed:
            auxR.run(-200)

        else:
            auxR.stop()

    wait(100)