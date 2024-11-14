from pybricks.parameters import Stop
from pybricks.tools import wait

#def code2():
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

#b.straight(100)
b.turn(-45)
#b.settings(straight_speed=1000)
b.straight(650)
b.straight(-650)