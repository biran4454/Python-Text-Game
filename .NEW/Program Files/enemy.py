import save
import sys
import random
random.seed()
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def eq(cmd, s):
    return cmd.lower() == s.lower()
def rprint(text): #Print through stderr. Pros: makes red text! Yay!
    sys.stderr.write(text)

enemyName = ""
enemyAttack = 0
enemyHealth = 0
enemyAccuracy = 0
playerAttack = 0
playerHealth = 0
playerAccuracy = 0
def checkEnemyHealth(locationID):
    try:
        with open("VariableData\\EnemyHealth\\%s.txt" % str(locationID), "r") as f:
            return int(f.readline())
    except OSError:
        return -1
def setEnemyHealth(locationID, value):
    try:
        with open("VariableData\\EnemyHealth\\%s.txt" % str(locationID), "w") as f:
            f.write(str(value))
    except OSError:
        rprint("THIS ERROR SHOULD NOT BE PRINTED. IF IT IS THEN PLEASE CONTACT THE GAME MAKER\n")
def attackPlayer():
    result = random.randrange(10)
    if(result > enemyAccuracy):
        effect = random.randrange(max(enemyAttack - 10, 4), max(enemyAttack + 10, 6)) #No negative damage!
        rprint("It attacks and does " + str(effect) + " damage\n")
        return effect
    else:
        print("It attacks, but misses")
        return 0
def attackEnemy():
    result = random.randrange(10)
    if(result > playerAccuracy):
        effect = random.randrange(max(playerAttack - 10, 4), max(playerAttack + 10, 6))
        rprint("You attack and do " + str(effect) + " damage\n")
        return effect
    else:
        print("You attack, but miss")
        return 0

def loadEnemy(fileID): #Returns 0 if player dead, 1 if alive, 2 if running away
    try:
        with open("FixedData\\Locations\\%s.txt" % fileID) as f:
            for i in range(int(f.readline()[:-1])): #Skip the first lines
                f.readline()
            for i in range(int(f.readline())):
                f.readline()
            for i in range(int(f.readline()) * 8):
                f.readline()
            f.readline()
            enemyName = f.readline()[:-1] #Set enemy stats
            enemyAccuracy = int(f.readline())
            enemyInitHealth = int(f.readline())
            enemyAttack = int(f.readline())
            h = checkEnemyHealth(fileID)
            if(h != -1):
                enemyHealth = h
                f.readline()
            else:
                enemyHealth = enemyInitHealth
            playerAttack = save.getPlayerValue("attack")
            playerHealth = save.getPlayerValue("health")
            playerAccuracy = save.getPlayerValue("accuracy")
            playerInitHealth = save.gPlayerInitHealth()
            print("Enemy found: " + enemyName)
            while True:
                playerHealthDiff = playerHealth
                playerHealth -= attackPlayer()
                if(playerHealth <= 0): #If dead
                    return 0
                enemyHealthDiff = enemyHealth
                enemyHealth -= attackEnemy()
                if(enemyHealth <= 0):
                    print("You defeated the " + enemyName + "!")
                    setEnemyHealth(fileID, enemyHealth)
                    save.saveValue("health", playerHealth)
                    return 1
                print("Your health:  ", end="")
                for i in range(int(playerHealth / playerInitHealth * 40)):
                    print("▅", end="")
                for i in range(int((playerHealthDiff - playerHealth) / playerInitHealth * 40)):
                    sys.stdout.shell.write("▅", "STRING")
                for i in range(int((playerInitHealth - playerHealthDiff) / playerInitHealth * 40)):
                    rprint("▅")
                print(" " + str(playerHealth))
                
                print("Enemy health: ", end="")
                if(enemyHealth / enemyInitHealth * 100 > 20):
                    for i in range(int(enemyHealth / enemyInitHealth * 40)):
                        print("▅", end="")
                    for i in range(int((enemyHealthDiff - enemyHealth) / enemyInitHealth * 40)):
                        sys.stdout.shell.write("▅", "STRING")
                    for i in range(int((enemyInitHealth - enemyHealthDiff) / enemyInitHealth * 40)):
                        rprint("▅")
                    print(" " + str(enemyHealth))
                print()
                attackCmd = input("Command? (Escape, Medi, Use, [enter])\n>>> ").lower()
                try:
                    firstCmdIndex = attackCmd.index(' ') #Get first word
                except ValueError:
                    firstCmdIndex = len(attackCmd)
                firstCmd = attackCmd[:firstCmdIndex].lower()
                
                if(firstCmd == "escape"):
                    save.saveValue("health", playerHealth)
                    setEnemyHealth(fileID, enemyHealth)
                    return 2
                if(firstCmd == "medi"): #Health pack
                    if(inventory.count("medipack") > 0 or inventory.count("Medipack") > 0):
                        playerHealth += 20
                        playerHealth = min(playerHealth, 60)
                if(firstCmd == "use"): #Extra attack
                    if(firstCmdIndex != -1):
                        secondCmdIndex = len(attackCmd)
                        secondCmd = attackCmd[firstCmdIndex + 1:secondCmdIndex].lower()
                        if(eq(secondCmd, "rocks")):
                            if(inventory.count("rocks") > 0):
                                attackEnemy()
                            else:
                                rprint("You don't have " + secondCmd + ".\n")
                        else:
                            rprint("You can't use " + secondCmd + ".\n")
                    else:
                        rprint("Nothing selected to use. Continuing.\n")
            
    except OSError:
        rprint("File does not exist. Please contact the program maker.\n")
        return 1

