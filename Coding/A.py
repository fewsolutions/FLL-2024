from pybricks.parameters import Stop
from pybricks.tools import wait

#def code1():
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

#365 degrees for full turn if using grabber attachment

b.straight(100)
b.turn(80)
b.straight(300)
b.turn(-20)
b.straight(200)
b.turn(30)
b.straight(650)
b.settings(turn_rate=50)
b.turn(-40)
b.settings(turn_rate=150)
b.straight(20)
b.turn(40)
b.straight(250)
b.straight(-100)
b.turn(-90)
b.straight(200)
