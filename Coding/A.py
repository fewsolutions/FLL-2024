from pybricks.parameters import Stop
from pybricks.tools import wait

#def code2():
#Coral run
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

b.use_gyro(True)

auxL.run_angle(300, -270)

b.straight(250)
b.turn(45)
b.straight(425)
b.turn(-45)
b.straight(150)
b.turn(-90)
b.straight(100)
b.straight(-90)
b.turn(45)
b.straight(110)
auxL.run_angle(400, 350)
auxL.run_angle(400, -170)
b.straight(-50)
b.turn(-20)
b.straight(40)
auxL.run_angle(400, -180)
