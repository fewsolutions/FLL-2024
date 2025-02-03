from pybricks.parameters import Stop
from pybricks.tools import wait

def code6():
    # Submarine run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.turn(-30)
    b.straight(800)
    b.turn(-40)
    b.straight(200)
    b.turn(-30)
    b.turn(60)
    b.straight(300)
    wait(500)
    b.straight(-150)
    b.turn(-45)
    b.straight(-400)
    b.turn(70)
    b.straight(-700)


#code6()