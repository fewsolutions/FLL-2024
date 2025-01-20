from pybricks.parameters import Stop
from pybricks.tools import wait


# New Coral run
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

auxR.run_angle(400, 200)
b.turn(24)
b.straight(735)
b.turn(-117)
auxR.run_angle(400, -90)
b.straight(55)
b.straight(-10)
