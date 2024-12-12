from pybricks.parameters import Stop
from pybricks.tools import wait

#def code2():
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

b.turn(-42)
b.straight(500)
b.straight(-350)
b.turn(24)
b.straight(380)
b.turn(35)
b.straight(135)
b.settings(turn_rate=50)
b.turn(-87)
b.straight(400)
b.turn(-18)
b.straight(200)
