from pybricks.parameters import Stop
from pybricks.tools import wait, multitask, run_task


# New Coral run
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()
b.use_gyro(True)

auxR.run_angle(400, 150)
b.straight(188)
b.turn(36)
b.straight(625)
b.turn(-125)
b.straight(150)
b.straight(-78)
auxR.run_angle(400, -65)
b.straight(60)
auxR.run_angle(400, 80)
b.straight(-120)
b.turn(30)
b.straight(208)
b.straight(-167)
b.turn(88)
auxR.run_angle(400, -50)
b.straight(55)
auxR.run_angle(400, -28)
b.straight(-124)
b.turn(-15)
b.straight(45)
auxR.run_angle(400, -38)
b.straight(41)
auxR.run_angle(400, -116)
auxR.run_angle(400, 95)
