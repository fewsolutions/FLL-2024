from pybricks.parameters import Stop
from pybricks.tools import wait

def code3():
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)


    auxL.run_target(500, 90)