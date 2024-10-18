from pybricks.parameters import Button, Color
from pybricks.tools import wait
from importlib import import_module

from setup import setup

#IMPORTANT
#This is where each code is associated with a letter and colour for the colour sensor
#Format: {"CodeLetter": [Color.COLOR, codereference]}
codesdict = {"A": [Color.RED, code1], "B": [Color.BLUE, code2], "C": [Color.GREEN, code3]}

#Setup the hub, motors, colour sensor and DriveBase
hub, auxL, auxR, auxCS, base = setup()



#import codes
'''def code1():
    hub.light.on(Color.RED)
    wait(200)
    hub.light.off

def code2():
    hub.light.on(Color.BLUE)
    wait(200)
    hub.light.off

def code3():
    hub.light.on(Color.GREEN)
    wait(200)
    hub.light.off'''



#import codes from the codes dictionary instead of manually importing them
for key, value in codesdict.items():
    module_name = key
    code_name = value[1]
    module = import_module(module_name)
    globals()[code_name] = getattr(module, code_name)

selected = 0

def menu(codesdict):
    #sets up some variables
    global selected
    lastsensor = None
    codes = list(codesdict.keys())
    codecount = len(codes) - 1

    #Main menu loop
    while True:
        print(selected)
        #Display Code Character
        hub.display.char(codes[selected])
        #Check what colour the colour sensor can see
        attachsensed = sensor.color(surface=True)
        #Check if this colour is associated with any codes
        if attachsensed in {key: value[0] for key, value in codesdict.items()}.values():
            #Check if this colour has already been detected and if so don't do anything
            if attachsensed != lastsensor:
                #Set selected to the code the colour detected is associated with
                #Edit: added + 1 to the index to fix the index out of range error
                selected = (list({key: value[0] for key, value in codesdict.items()}.values()).index(attachsensed)) + 1
                #Remember what the last colour sensed was
                lastsensor = attachsensed
                print(f"Colour sensor used {attachsensed}")
                continue

        #Check which buttons have been pressed
        pressed = hub.buttons.pressed()
        #Check if the Right button has been pressed
        if Button.RIGHT in pressed:
            #Add one to the selected code variable, or if it is on the last, scroll back to the start
            if selected == codecount:
                selected = 0
            else:
                selected = selected + 1
            print("Right button")

        elif Button.LEFT in pressed:
            if selected == 0:
                selected = codecount
            else:
                selected = selected - 1
            print("Left button")

        elif Button.CENTER in pressed:
            return codes[selected]

        wait(125)
def main(codesdict):
    while True:
        code = menu(codesdict)

        if code in codesdict:
            codesdict[code][1]()

main(codesdict)