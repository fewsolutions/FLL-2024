from pybricks.parameters import Stop
from pybricks.tools import wait, multitask, run_task


# New Coral run
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

auxR.run_angle(400, 197)
b.settings(straight_speed=100, straight_acceleration=100)
b.straight(280)
b.settings(straight_speed=750, straight_acceleration=500)
b.straight(-83)
b.turn(37)
b.straight(580)
b.turn(-129)
auxR.run_angle(400, -89)
wait(25)
b.straight(97)
auxR.run_angle(400, 50)
b.straight(-102)