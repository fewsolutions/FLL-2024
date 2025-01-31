from pybricks.parameters import Stop
from pybricks.tools import wait, multitask, run_task


# New Coral run
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

auxR.run_angle(400, 197)
b.straight(197)
b.turn(37)
b.straight(615)
b.turn(-129)
auxR.run_angle(400, -99)
wait(25)
b.settings(straight_acceleration=100)
b.straight(165)
b.settings(straight_acceleration=500)
auxR.run_angle(400, 50)
b.straight(-102)
b.turn(38)
b.straight(170)

b.straight(-138)
b.turn(87)
auxR.run_angle(400, -29)
b.straight(37)

auxR.run_angle(400, -28)
b.straight(-77)
b.turn(-10)
b.straight(41)
auxR.run_angle(400, -127)






'''b.straight(-250)
b.settings(turn_acceleration=100, straight_acceleration=100)
b.turn(53)
auxR.run_angle(200, -20)
b.straight(105)
auxR.run_angle(200, -16)
b.settings(turn_acceleration=200, straight_acceleration=500)
b.straight(-130)

auxR.run_angle(400, -45)
b.straight(97)
auxR.run_angle(400, -110)
b.straight(-110)'''




'''b.straight(-100)
b.turn(47)
b.straight(310)
auxR.run_angle(400, 90)


b.turn(64)
b.settings(straight_speed=750)
b.straight(1036)
b.turn(64)
b.straight(531)

auxL.run_target(400, 0)
auxR.run_target(400, 0)'''