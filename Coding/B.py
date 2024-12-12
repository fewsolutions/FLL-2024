from pybricks.parameters import Stop
from pybricks.tools import wait

#def code2():
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

b.turn(-42)
b.straight(500)
b.straight(-350)
b.turn(22)
b.straight(400)
b.turn(30)
b.straight(200)
b.settings(straight_speed=200)
b.curve(200, 180)

#b.turn(35)
#b.straight(200)
#b.straight(-100)
#b.turn(-45)
#b.straight(120)