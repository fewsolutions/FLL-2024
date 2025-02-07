from pybricks.parameters import Stop
from pybricks.tools import wait

def code4():
    # Radar run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    auxL.run_angle(400, -200)
    b.turn(-17.85)
    b.straight(870)
    auxL.run_angle(400, 192)
    #If arm gets stuck in radar
    #b.straight(30)
    #b.straight(-215)
    b.straight(-245)
    auxL.run_angle(400, -68)
    b.turn(80)
    b.straight(0)
    auxL.run_angle(400, 100)
    b.straight(-100)
    b.turn(-82)
    b.use_gyro(False)
    b.straight(-595)
    b.turn(50)

    
    auxL.run_target(400, 0)
    auxR.run_target(400, 0)

#code4()