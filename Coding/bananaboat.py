from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    #BananaBoat run
    from Codes import setup
    hub, b, auxL, auxR, colorsensor = setup()

    b.use_gyro(True)

    b.straight(220, then=Stop.NONE)
    b.curve(500, 16)
    b.use_gyro(False)
    b.straight(-350)

    #b.turn(-24)
    #b.straight(155)
    #b.turn(19.5)
    #b.straight(215)
    #b.straight(-345)

    #b.turn(-60)
    #b.straight(325)
    #b.turn(80)
    #b.straight(100)

#code1()