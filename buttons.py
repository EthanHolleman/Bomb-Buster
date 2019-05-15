import time

def buttons(color, word):
    ABORT = "abort"
    DETONATE = "detonate"
    HOLD = "hold"
    color = color.lower()
    word = word.lower()
    bats = input("Enter number of batteries on bomb ")

    if color == "b" and word == ABORT:
        press()
    elif bats > 1 and word == DETONATE:
        return "Press and release immediatly"
    elif color == "w":
        car = input("Is there a LIT indicator with label CAR? Type y for yes n for no ")
        if car == y:
            press()
    elif bats > 2:
        frk = input("Is there a LIT indicator with label FRK? Type y for yes n for no ")
        if frk == y:
            return "Press and release immediatly"
    elif color == "y":
        press()
    elif color == "r" and word == HOLD:
        return "Press and release immediatly"
    else:
        press()


def press():
    print("Press and hold the button")
    time.sleep(0.5)
    light = input("Enter color of the first letter of the color of colored strip")
    light = light.lower()

    if light == "b":
        return "Release when timer has 4 in any position"
    elif light == "w":
        return "Release when timer has 1 in any position"
    elif light == "y":
        return "Release when timer has 5 in any position"
    else:
        return "Release when timer has 1 in any position"
