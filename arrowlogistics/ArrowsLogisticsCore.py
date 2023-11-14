# ArrowLogistics by Senko

# Library/high-level programming language for logics-arrows.io. Logic-Arrows developer - Onigiri.

# Thanks Xeonys, KtoTo for parsing the save system.

# You can modify the code and distribute it for free. Selling, issuing an unchanged code for your own is prohibited.

import base64


def encode(inp):
    numbers = list(map(int, inp.split()))
    byte_array = bytes(numbers)
    base64_string = base64.b64encode(byte_array).decode('utf-8')
    return base64_string


def setup(n):
    if int(n) < 10:
        output_ArrowLogistics = "0 0 " + str(n) + " 0" + " 0 0 0 0"
        return output_ArrowLogistics
    else:

        print("Setup(" + str(n) + ")")
        print("^^^^^^^^^^^^^^^^^^^^")
        print("cannot create up ten chunks")
        exit()


def tpr(typearl, pos, rotation):
    typeArrowLogistics = typearl
    posArrowLogistics = pos
    rotationArrowLogistics = rotation

    output = " " + " " + str(typeArrowLogistics) + " 0 " + str(posArrowLogistics) + " " + str(rotationArrowLogistics)

    return output


def chunknumber(n):
    a = " " + str(n) + " "
    return a


def counts(n):
    a = " " + str(n - 1) + " "
    return a


def ramgen():
    a = ""

    for i in range(1, 7):
        if i == 1:
            for iw in range(0, 16):
                if iw % 2:
                    a += tpr(3, iw, 3)

                else:
                    a += tpr(18, iw, 0)
        elif i == 2:
            for iw in range(0, 16):
                if iw % 2:
                    a += tpr(13, iw + 16, 3)

                else:
                    a += tpr(1, iw + 16, 0)

        elif i == 3:
            for iw in range(0, 16):
                if iw % 2:
                    a += tpr(13, iw + 32, 7)
        elif i == 4:
            for iw in range(0, 16):
                if iw % 2:
                    a += tpr(3, iw + 16 * 3, 3)

                else:
                    a += tpr(10, iw + 16 * 3, 0)
        elif i == 5:
            for iw in range(0, 16):
                if iw % 2:
                    pass

                else:
                    a += tpr(19, iw + 16 * 4, 0)
        elif i == 6:
            for iw in range(0, 16):
                if iw % 2:
                    pass

                else:
                    a += tpr(24, iw + 16 * 5, 0)

    return a


def peerbuild(filename):
    file_name = filename

    formatpeer = file_name.split(".")[1]

    outputbytearray = ""




    if formatpeer == "peer":
        with open(file_name, 'r') as file:
            lines = [line for line in file]

            for i in lines:




                if "arrow" in i:

                    command = i.replace("("," ").replace(")"," ").replace(",", " ").replace(";", " ").split(" ")

                    commandd = [item for item in command if item != ""]
                    commandss = [item for item in commandd if item != "\n"]
                    commands = [int(item) if item.isdigit() else item for item in commandss]



                    types = commands[1]

                    x = commands[2]

                    y = commands[3]

                    r = commands[4]

                    pos = x + (y*16)



                    outputbytearray += tpr(types, pos, r)



    else:
        print(f"ERROR: It is not possible to open a file with the format '{formatpeer}' try '.peer'")

    return outputbytearray