import code1, code2, code3



codesdict = {"A": ["Red", code1], "B": ["Blue", code2], "C": ["Green", code3]}


def menu(codesdict):
    selected = 0

    coloursense = input("Colour Sense: ")
    if coloursense in {key: value[0] for key, value in codesdict.items()}.values():
        selected = list({key: value[0] for key, value in codesdict.items()}.values()).index(coloursense)
    elif coloursense == "":
        pass
    else:
        print("Invalid input")
    codes = list(codesdict.keys())
    print(codes[selected])
    while True:
        arrows = input("Navigation: ")
        codecount = len(codes) - 1
        if arrows == "<":
            if selected <= 0:
                selected = codecount
            else:
                selected -= 1
            print(codes[selected])
        elif arrows == ">":
            if selected >= codecount:
                selected = 0
            else:
                selected += 1
            print(codes[selected])
        elif arrows == "/":
            return codes[selected]
        else:
            print("Invalid input")

while True:
    code = menu(codesdict)

    if code in codesdict:
        codesdict[code][1]()

    else:
        print("Invalid code")