import sys
def eq(cmd, s):
    return cmd.lower() == s.lower()
def rprint(text): #Print through stderr. Pros: makes red text! Yay!
    sys.stderr.write(text)

def setPlayerHealth(value):
    try:
        with open("variable data files\PlayerProperties\health.txt", "w") as f:
            f.write(str(value))
    except OSError:
        rprint("ERROR: PlayerProperties FOLDER NOT FOUND\n")
def getPlayerHealth():
    try:
        with open("variable data files\PlayerProperties\health.txt", "r") as f:
            return f.readline()
    except OSError:
        try:
            with open("fixed data files\PlayerHealth.txt", "r") as f:
                return f.readline()
        except OSError:
            return 60
def setPlayerAttack(value):
    try:
        with open("variable data files\PlayerProperties\attack.txt", "w") as f:
            f.write(str(value))
    except OSError:
        rprint("ERROR: PlayerProperties FOLDER NOT FOUND\n")
def getPlayerAttack():
    try:
        with open("variable data files\PlayerProperties\attack.txt", "r") as f:
            return f.readline()
    except OSError:
        try:
            with open("fixed data files\PlayerAttack.txt", "r") as f:
                return f.readline()
        except OSError:
            return 10
