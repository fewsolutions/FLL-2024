from pybricks.parameters import Stop
from pybricks.tools import wait

def code2():
    # Krill run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.turn(-45)
    b.straight(565)
    b.straight(-280)
    b.turn(37)
    b.straight(390)
    b.turn(34)
    b.straight(125)
    b.settings(turn_rate=75)
    b.turn(-100)
    b.settings(turn_rate=200)
    b.straight(350)
    b.turn(-25)
    b.straight(350)
    b.turn(18)
    b.straight(277)
    b.turn(-17)
    b.straight(298)
    b.turn(-56)
    b.straight(620)

    #Reset for next run
    auxL.run_target(400, 0)
    
    auxR.run_target(400, 0)

code2()