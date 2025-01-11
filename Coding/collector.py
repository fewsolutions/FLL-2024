from pybricks.parameters import Stop
from pybricks.tools import wait

#def code2():
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

b.turn(-42)
b.straight(500)
b.straight(-350)
b.turn(32)
b.straight(350)
b.turn(40)
b.straight(60)
b.turn(100)
b.straight(340)
b.turn(50)
b.straight(250)