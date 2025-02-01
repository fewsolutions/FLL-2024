from pybricks.parameters import Stop
from pybricks.tools import wait

def code5():
    # Radar run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    auxL.run_angle(400, -200)
    b.turn(-17.8)
    b.straight(840)
    auxL.run_angle(400, 172)
    b.straight(-240)
    auxL.run_angle(400, -68)
    b.turn(74)
    auxL.run_angle(400, 100)
    b.straight(-100)
    b.turn(-82)
    b.straight(-595)

    
    auxL.run_target(400, 0)
    auxR.run_target(400, 0)

code5()