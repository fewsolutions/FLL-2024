from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    #BananaBoat run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()

    b.use_gyro(True)


    b.turn(-25)
    b.straight(165)
    b.turn(19)
    b.straight(175)
    b.straight(-345)

code1()