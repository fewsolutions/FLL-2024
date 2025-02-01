from pybricks.parameters import Stop
from pybricks.tools import wait, multitask, run_task


# Whale run
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

def code4():
    b.turn(-30)
    b.straight(682)
    b.turn(72)
    wait(100)
    b.settings(straight_speed=750, straight_acceleration=750)
    b.straight(325)
    wait(500)

    b.straight(-150)
    b.turn(-70)
    b.straight(-730)
    b.use_gyro(False)
    b.turn(70)

code4()