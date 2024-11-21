from pybricks.parameters import Stop
from pybricks.tools import wait

#def code2():
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

b.turn(-55)
b.straight(-500)
b.straight(350)
