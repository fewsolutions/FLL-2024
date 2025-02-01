from pybricks.parameters import Button, Color
from pybricks.tools import wait

from codes import setup, reset, ready

import Bananaboat, Krill, Coral, Whale, remotecontrol

#IMPORTANT
#This is where each code is associated with a letter and colour for the colour sensor
#Format: [("LETTER", Color.COLOUR, Filename.codename)]
codeslist = [("1", Color.RED, Bananaboat.code1), ("2", Color.BLUE, Krill.code2), ("3", Color.GREEN, Coral.code3), ("4", Color.YELLOW, Whale.code4), ("R", Color.WHITE, remotecontrol.remotecode)]

#Setup the hub, motors, colour sensor and DriveBase
hub, base, auxL, auxR, colorsensor = setup()

selected = 0

def menu(codeslist):
    #sets up some variables
    global selected
    lastsensor = None
    codes = [item[2] for item in codeslist]
    codecount = len(codes) - 1

    #Main menu loop
    while True:
        
        wait(150)

        #print(selected)
        #Display Code Character
        hub.display.char(codeslist[selected][0])

        #Colour sensor attachment detection
        if colorsensor != None:

            #Check what colour the colour sensor can see
            colorsensed = colorsensor.color(surface=True)

            #Check if this colour is associated with any codes
            if colorsensed in [item[1] for item in codeslist]:

                #Check if this colour has already been detected and if so don't do anything
                if colorsensed != lastsensor:
                    #Set selected to the code the colour detected is associated with
                    #Edit: added + 1 to the index to fix the index out of range error
                    selected = [item[1] for item in codeslist].index(colorsensed)
                    #Remember what the last colour sensed was
                    lastsensor = colorsensed
                    #print(f"Colour sensor used {colorsensed}")
                    continue

        else:
            wait(25)

        #Check which buttons have been pressed
        pressed = hub.buttons.pressed()

        if Button.RIGHT in pressed:
            if selected == codecount:
                selected = 0
            else:
                selected = selected + 1

        elif Button.LEFT in pressed:
            if selected == 0:
                selected = codecount
            else:
                selected = selected - 1
            

        elif Button.CENTER in pressed:
            return selected


def main(codeslist):
    while True:
        reset()

        #Run the menu
        codeindex = menu(codeslist)

        ready()

        codeslist[codeindex][2]()

        

if __name__ == "__main__":
    main(codeslist)