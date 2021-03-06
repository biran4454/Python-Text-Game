import sys
import random
import playerSet
enemyName = ""
enemyAttack = 20
enemyHealth = 50
enemyAccuracy = 6
playerAttack = playerSet.getPlayerAttack()
playerHealth = playerSet.getPlayerHealth()
playerAccuracy = 7
def eq(cmd, s):
    return cmd.lower() == s.lower()
def rprint(text): #Print through stderr. Pros: makes red text! Yay!
    sys.stderr.write(text)
def checkEnemyHealth(locationID):
    try:
        with open("variable data files/EnemyHealth/%s.txt" % str(locationID), "r") as f:
            return int(f.readline())
    except OSError:
        return -1
def setEnemyHealth(locationID, value):
    try:
        with open("variable data files/EnemyHealth/%s.txt" % str(locationID), "w") as f:
            f.write(str(value))
    except OSError:
        rprint("THIS ERROR SHOULD NOT BE PRINTED. IF IT IS THEN PLEASE CONTACT THE GAME MAKER\n")

def attackPlayer():
    result = random.randrange(10) #Used for hit / miss calc
    if(result <= enemyAccuracy):
        effect = random.randrange(max(enemyAttack - 20, 4), max(enemyAttack, 6)) #No negative damage!
        result = random.randrange(10)
        rprint("It attacks and does " + str(effect) + " damage\n")
        return effect
    else:
        print("It attacks, but misses")
        return 0

def attackEnemy():
    result = random.randrange(10)
    if(result <= playerAccuracy):
        effect = random.randrange(max(playerAttack - 20, 4), max(playerAttack, 6))
        result = random.randrange(10)
        rprint("You attack and do " + str(effect) + " damage\n")
        return effect
    else:
        print("You attack, but miss")
        return 0

def loadEnemy(fileID): #Returns 0 if player dead, 1 if alive, 2 if running away
    try:
        with open("fixed data files/"+ fileID + ".txt") as f:
            for i in range(int(f.readline()[:-1])): #Skip the first lines
                f.readline()
            for i in range(int(f.readline())):
                f.readline()
            for i in range(int(f.readline()) * 8):
                f.readline()
            f.readline()
            enemyName = f.readline()[:-1] #Set enemy stats
            print("Enemy found: " + enemyName)
            enemyAttack = int(f.readline())
            h = checkEnemyHealth(fileID)
            if(h != -1):
                enemyHealth = h
                f.readline()
            else:
                enemyHealth = int(f.readline())
            enemyAccuracy = int(f.readline())
            playerAttack = playerSet.getPlayerAttack()
            playerHealth = playerSet.getPlayerHealth()
            playerAccuracy = 7
            while True:
                playerHealth -= attackPlayer()
                if(playerHealth <= 0): #If dead
                    return 0
                enemyHealth -= attackEnemy()
                if(enemyHealth <= 0):
                    print("You defeated the " + enemyName + "!")
                    setEnemyHealth(fileID, enemyHealth)
                    return 1
                print("Your health:  ", end="")
                if(playerHealth > 20): #TODO: greater than percentage of start health
                    for i in range(playerHealth):
                        print("▅", end="") #Print health bar
                else:
                    for i in range(playerHealth):
                        rprint("▅")
                print()
                print("Enemy health: ", end="")
                if(enemyHealth > 20):
                    for i in range(enemyHealth):
                        print("▅", end="")
                else:
                    for i in range(enemyHealth):
                        rprint("▅")
                print()
                attackCmd = input("Command? (Escape, Medi, Use, [enter])\n>>> ").lower()
                try:
                    firstCmdIndex = attackCmd.index(' ') #Get first word
                except ValueError:
                    firstCmdIndex = len(attackCmd)
                firstCmd = attackCmd[:firstCmdIndex].lower()
                
                if(firstCmd == "escape"):
                    playerSet.setPlayerHealth(playerHealth)
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
                                rprint("You don't have " + secondCmd + ". \n")
                        else:
                            rprint("You can't use " + secondCmd + ". \n")
                    else:
                        rprint("Nothing selected to use. Continuing.\n")
            
    except OSError:
        rprint("File does not exist. Please contact the program maker.\n")
        return 1
