#problem with black or blue wires
def solveWires(wireString):
    wires = wireOrder.lower().split(" ")
    length = len(wireOrder)


    if length == 3:
        if "r" not in wires:
            return "Cut the second wire"
        elif wires[-1] == "w":
            return "Cut the last wire"
        elif wires.count("b") > 1:
            return "Cut the last blue wire"
        else:
            return "Cut the last wire"

    elif length == 4:
        if wires.count("r") > 1:
            serial = input("Enter last number of serial number ")
            if serial % 2 == 1:
                return "cut the last wire"
        elif wires[-1] == 'y' and wires.count('r') == 0:
            return "Cut the first wire"
        elif wires.count("b") == 1:
            return "Cut the first wire"
        elif wires.count('y') > 1:
            return "Cut the last wire"
        else:
            return "Cut the first wire"

    elif length = 5:
        if wires[-1] == 'bl':
            serial = input("Enter last number of serial number ")
            if serial % 2 == 1:
                return "Cut the fourth wire"
        elif wires.count('r') == 1 and wires.count('y') > 1:
            return "Cut the first wire"
        elif wires.count('bl') == 0:
            return "Cut the second wire"
        else:
            return "Cut the first wire"
    else:
        if wires.count('y') == 0:
            serial = input("Enter last number of serial number ")
            if serial % 2 == 1:
                return "Cut the third wire"
        elif wires.count('y') == 1 and wires.count('w') > 1:
            return "Cut the fourth wire"
        elif wires.count('r') == 0:
            return "Cut the last wire"
        else:
            return "Cut the fourth wire"
