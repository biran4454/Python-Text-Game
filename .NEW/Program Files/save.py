import sys
def saveValue(name, value):
    try:
        with open("VariableData\\Player\\%s.val" % name, "w") as f:
            f.write(str(value))
    except OSError:
        return -1
def getPlayerValue(name):
    try:
        with open("VariableData\\Player\\%s.val" % name, "r") as f:
            return int(f.read())
    except OSError:
        try:
            with open("FixedData\\PlayerProperties\\%s.val" % name, "r") as f:
                return int(f.read())
        except OSError:
            print("Could not find file")
            return 0

def sPlayerInventory(value):
    try:
        with open(r"VariableData\Player\inventory.list", "a") as f:
            f.write(str(value))
    except OSError:
        return -1
def gPlayerInventory():
    try:
        with open(r"VariableData\Player\inventory.list", "r") as f:
            return f.read().split("\n")
    except OSError:
        print("\nInventory not found\n")
        return []
def gPlayerInitHealth():
    try:
        with open("FixedData\\PlayerProperties\\health.val", "r") as f:
            return int(f.read())
    except OSError:
        return 60
