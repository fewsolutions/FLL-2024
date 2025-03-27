from pybricks.parameters import Stop
from pybricks.tools import wait

def code6():
    # Submarine run
    from Codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.turn(-30)
    b.straight(770)
    b.turn(-40)
    b.straight(260)
    b.turn(-30)
    b.turn(55)
    b.straight(300)
    wait(500)
    b.straight(-150)
    b.turn(-45)
    b.straight(-450)
    b.turn(90)
    b.straight(-750)
 

#code6()