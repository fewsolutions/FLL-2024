from pybricks.parameters import Stop
from pybricks.tools import wait, multitask, run_task


# New Coral run
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()



async def upL():
    await auxL.run_angle(400, -300)

async def upR():
    await auxR.run_angle(400, 200)

run_task(multitask(upL(), upR()))


b.straight(250)
b.turn(45)
b.straight(425)
b.turn(-45)
b.straight(120)
b.turn(-90)
auxR.run_angle(400, -120)
b.straight(130)
b.straight(-10)
auxR.run_angle(400, 150)
b.straight(-125)
b.turn(34)
b.straight(205)
b.straight(-253)
