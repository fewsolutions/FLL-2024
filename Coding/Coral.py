from pybricks.parameters import Stop
from pybricks.tools import wait

def code3():
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
    b.turn(33)
    b.straight(189)
    b.straight(-164)

    auxL.run_angle(400, 162)
    b.straight(62)
    auxL.run_angle(400, -32)
    b.straight(-220)

    b.turn(68)
    b.straight(100)
    b.turn(19)

    '''
    auxL.run_angle(400, 165)
    b.turn(-3)
    b.straight(78)
    auxL.run_angle(400, -29)
    b.straight(-203)
    b.turn(94)
    b.straight(69)
    b.turn(-24)
    b.straight(23)'''

code3()