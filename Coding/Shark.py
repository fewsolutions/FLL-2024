from pybricks.parameters import Stop
from pybricks.tools import wait

def code3():
    # Shark run
    from Codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    auxR.run_angle(200, 171)
    b.turn(27)
    b.straight(766)
    b.turn(-114)
    b.straight(184)
    b.straight(-112)
    b.turn(31.4)
    b.straight(225)
    b.straight(-143)
    b.turn(103)
    auxR.run_angle(400, -180)
    b.turn(41)
    b.settings(straight_speed=150)
    b.straight(147)
    b.settings(straight_speed=750)
    b.turn(-44)
    auxR.run_angle(400, 57)
    b.straight(232)
    auxR.run_angle(400, 138)
    b.turn(56)
    b.straight(1040)
    b.turn(64)
    b.straight(531)
    auxL.run_target(400, 0)
    auxR.run_target(400, 0)

#code3()