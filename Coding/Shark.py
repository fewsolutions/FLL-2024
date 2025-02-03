from pybricks.parameters import Stop
from pybricks.tools import wait

def code3():
    # Shark run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    auxR.run_angle(200, 171)
    b.turn(27)
    b.straight(763)
    b.turn(-114)
    b.straight(168)
    b.straight(-112)
    b.turn(32)
    b.straight(200)

    b.straight(-133)
    b.turn(100)
    auxR.run_angle(400, -180)
    b.turn(44.5)


    b.settings(straight_speed=150)
    b.straight(147)
    b.settings(straight_speed=750)
    b.turn(-46)
    auxR.run_angle(400, 70)
    b.straight(232)
    auxR.run_angle(400, 138)

    b.turn(59)
    b.straight(1040)
    b.turn(64)
    b.straight(531)

    auxL.run_target(400, 0)
    auxR.run_target(400, 0)

    '''b.settings(straight_speed=100)
    b.straight(140)
    b.settings(straight_speed=750)
    b.turn(-50)
    auxR.run_angle(400, 100)
    b.straight(237)
    '''
    
    '''b.straight(52)
    auxR.run_angle(600, -170)
    auxR.run_angle(400, 65)
    b.turn(49)
    b.straight(300)
    auxR.run_angle(400, 210)
    b.turn(60)
    b.straight(993)
    b.turn(63)
    b.straight(550)'''
 
#code3()