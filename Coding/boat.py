from pybricks.parameters import Stop
from pybricks.tools import wait

def code7():
    # Boat run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.straight(311)
    auxR.run_angle(400, -120)
    auxR.run_angle(200, 180)
    b.straight(-155)
    wait(250)
    b.straight(145)
    auxR.run_angle(400, -130)
    auxR.run_angle(200, 171)
    b.straight(-100)
    wait(250)
    b.straight(115)
    auxR.run_angle(400, -120)

    auxR.run_angle(200, 162)
    b.straight(-163)
code7()
