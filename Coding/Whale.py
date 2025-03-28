from pybricks.parameters import Stop
from pybricks.tools import wait, multitask, run_task


# Whale run
from Codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

def code5():
    b.settings(turn_acceleration=750, turn_rate=750)
    b.turn(-30)
    b.straight(682)
    b.turn(72)
    wait(100)
    b.settings(straight_speed=250, straight_acceleration=750)
    b.straight(500)
    wait(500)
    b.settings(straight_speed=750, straight_acceleration=750)

    	
    b.use_gyro(False)
    b.straight(-200)
    b.turn(-180)
    b.straight(-730)
    b.turn(70)

code5()
