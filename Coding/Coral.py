from pybricks.parameters import Stop
from pybricks.tools import wait

def code3():
    # Coral run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.settings(straight_acceleration=300, straight_speed=300, turn_rate=300, turn_acceleration=300)
    auxR.run_angle(200, 171)
    b.turn(27)
    b.straight(763)
    b.turn(-112.5)
    auxR.run_angle(200, -74.5)
    b.straight(168)
    auxR.run_angle(100, 56)
    auxR.run_angle(100, -29)
    b.straight(-112)
    b.turn(34)
    b.straight(200)
    b.straight(-288)
    b.turn(47)
    b.settings(straight_acceleration=100, straight_speed=100)
    b.straight(120)
    b.settings(straight_acceleration=500, straight_speed=750)

    auxR.run_angle(200, -33)
    b.straight(-83)
    b.turn(45)
    auxR.run_angle(200, -29)
    b.straight(306)
    auxR.run_angle(200, 121)
    b.turn(58)
    b.straight(955)
    b.turn(60)
    b.straight(573)


code3()

