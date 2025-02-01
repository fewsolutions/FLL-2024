from pybricks.parameters import Stop
from pybricks.tools import wait

def code3():
    # Shark run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    auxR.run_angle(200, 171)
    b.turn(27)
    b.straight(763)
    b.turn(-114)
    b.straight(168)
    b.straight(-112)
    b.turn(32)
    b.straight(200)
    b.straight(-288)
    b.turn(50)

    b.straight(92)
    auxR.run_angle(400, -175)
    auxR.run_angle(400, 89)
    b.turn(46.5)
    b.straight(226)
    auxR.run_angle(400, 107)
    b.turn(57)
    b.straight(993)
    b.turn(63)
    b.straight(490)
 



code3()