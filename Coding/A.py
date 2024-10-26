from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    from codes import setup
    hub, base, auxL, auxR, colorsensor = setup()

    #base.straight(200, then=Stop.HOLD)
  
    base.turn(360)

    auxL.run_target(400, 90)
    auxR.run_target(400, 180)

    wait(5000)
