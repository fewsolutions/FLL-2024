from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    #BananaBoat run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()

    b.use_gyro(True)


    b.turn(-24)
    b.straight(135)
    b.turn(19.5)
    b.straight(215)
    b.straight(-345)

#code1()