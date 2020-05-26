"""
Text Adventure Game created by Biran4454
Code: Biran4454
Story: Biran4454
"""


"""
FILE STRUCTURE:

Number of text lines
Text line #1
Text line #2 etc.
Number of inventory items
Inventory items
Number of choices
Choice name #1
Is choice a door ("Door") or command? #1
Choice ID #1
Choice inventory requirement #1
Is choice inventory requirement shown? #1
Choice select text #1 etc.
Does door kill you? #1
Is there an enemy?
Enemy name
Enemy attack
Enemy health
Enemy accuracy
"""
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
    return(cmd.lower() == s.lower())
enemyName = ""
enemyAttack = 20
enemyHealth = 50
enemyAccuracy = 6
playerAttack = 10
playerHealth = 60
playerAccuracy = 7
def loadEnemy(fileID):
    try:
        with open(fileID + ".txt") as f:
            for i in range(int(f.readline()[:-1])):
                f.readline()
            for i in range(int(f.readline())):
                f.readline()
            for i in range(int(f.readline()) * 7):
                f.readline()
            f.readline()
            enemyName = f.readline()[:-1]
            print("Enemy found: " + enemyName)
            enemyAttack = int(f.readline())
            enemyHealth = int(f.readline())
            enemyAccuracy = int(f.readline())
            playerAttack = 10
            playerHealth = 60
            playerAccuracy = 7
            while enemyHealth > 0:
                playerHealth -= attackPlayer()
                if(playerHealth <= 0):
                    return(0)
                enemyHealth -= attackEnemy()
                if(enemyHealth <= 0):
                    print("You defeated the " + enemyName + "!")
                    return(1)
                print("Your health:  ", end="")
                if(playerHealth > 20):
                    for i in range(playerHealth):
                        print("█", end="")
                else:
                    for i in range(playerHealth):
                        sys.stderr.write("█")
                print()
                print("Enemy health: ", end="")
                if(enemyHealth > 20):
                    for i in range(enemyHealth):
                        print("█", end="")
                else:
                    for i in range(enemyHealth):
                        sys.stderr.write("█")
                print()
                if(input("Continue? (Press Y/N)\n>>> ").lower() == "n"):
                    return(2)
            
    except OSError:
        print("File does not exist")
        return(1)

def attackPlayer():
    result = random.randrange(10)
    if(result <= enemyAccuracy):
        effect = random.randrange(max(enemyAttack - 20, 4), max(enemyAttack, 6))
        result = random.randrange(10)
        sys.stderr.write("It attacks and does " + str(effect) + " damage\n")
        return(effect)
    else:
        print("It attacks, but misses")
        return(0)

def attackEnemy():
    result = random.randrange(10)
    if(result <= playerAccuracy):
        effect = random.randrange(max(playerAttack - 20, 4), max(playerAttack, 6))
        result = random.randrange(10)
        sys.stderr.write("You attack and do " + str(effect) + " damage\n")
        return(effect)
    else:
        print("You attack, but miss")
        return(0)
    
fileID = "00intro"
inventory = []
cont = True
lastID = "00intro"
while cont:
    choices = []
    choiceIsDoor = []
    choiceIDs = []
    choiceReq = []
    choiceReqShown = []
    choiceSel = []
    choiceDie = []
    try:
        with open(fileID + ".txt") as f:
            print("-- ID: " + fileID + " --\n") #Print location ID
            
            for i in range(int(f.readline()[:-1])): #Print story background
                line = f.readline()
                if line[:-1] == "+break":
                    input("Press enter to continue... ")
                else:
                    if len(line[:-1]) > 0 and line[0] == "+":
                        sys.stderr.write(line[1:])
                    else:
                        print(line[:-1])
            
            for i in range(int(f.readline())): #Add items to inventory
                inventory.append(f.readline()[:-1])
            
            choiceLen = int(f.readline()[:-1])
            for i in range(choiceLen): #Populate possible choices
                choices.append(f.readline()[:-1].lower())
                choiceIsDoor.append(f.readline()[:-1] == "1")
                choiceIDs.append(f.readline()[:-1])
                choiceReq.append(f.readline()[:-1])
                choiceReqShown.append(f.readline()[:-1])
                choiceSel.append(f.readline()[:-1])
                choiceDie.append(f.readline()[:-1])
            print()
            isNextDoor = False
            nextDoor = -1
            if(f.readline()[:-1] == "True"):
                attackResult = loadEnemy(fileID)
                if(attackResult == 0):
                    sys.stderr.write("You died.\n")
                    input("Press enter to continue...\n")
                    sys.stderr.write("PRESS CANCEL IF IN PYSHELL\n")
                    exit("User died")
                    cont = False
                if(attackResult == 2):
                    isNextDoor = True
                    nextDoor = lastID
                    lastID = fileID
            while (not isNextDoor):
                print("Enter command")
                command = input(">>> ")
                try:
                    firstCmdIndex = command.index(' ') #Get first word
                except ValueError:
                    firstCmdIndex = len(command)
                firstCmd = command[:firstCmdIndex]
                if eq(firstCmd, "inventory"): #If first word is inventory
                    print("You have:")
                    print(str(inventory)[1:-1], sep="\n")
                if eq(firstCmd, "exit") or eq(firstCmd, "quit"): #If first word is exit or quit
                    sys.stderr.write("PRESS CANCEL IF IN PYSHELL\n")
                    exit("User selected exit game")
                if eq(firstCmd, "input"): #If the user wants to move
                    if(firstCmdIndex != -1):
                        secondCmdIndex = len(command)
                        secondCmd = command[firstCmdIndex + 1:secondCmdIndex].lower()
                        try:
                            moveChoice = choices.index(secondCmd)
                            if(choiceReq[moveChoice] == "" or inventory.count(choiceReq[moveChoice]) > 0):
                                if(choiceDie[moveChoice] == "True"):
                                    print(choiceSel[moveChoice])
                                    sys.stderr.write("You died.\n")
                                    input("Press enter to continue...\n")
                                    sys.stderr.write("PRESS CANCEL IF IN PYSHELL\n")
                                    exit("User died")
                                    cont = False
                                else:
                                    if(choiceIsDoor[moveChoice]): #If its a door open it
                                        nextDoor = choiceIDs[moveChoice]
                                        isNextDoor = True
                                        print(choiceSel[moveChoice])
                                        input("Press enter to continue...\n")
                                        lastID = fileID
                                    else:
                                        print(choiceSel[moveChoice]) #Otherwise just print the text
                            else:
                                if(choiceReqShown[moveChoice] == "True"):
                                    sys.stderr.write("You need an item to do this: " + choiceReq[moveChoice] + "\n")
                                else:
                                    sys.stderr.write("You can't do that now\n")
                        except ValueError:
                            sys.stderr.write("The location \"" + secondCmd + "\" doesn't exist!\n")
                    else:
                        sys.stderr.write("You need to choose somewhere to move to!\n")
                
            
            fileID = nextDoor
    except ValueError as e:
        print()
        sys.stderr.write("An error has ocurred.\n")
        print()
        print("Please contact the game maker with the following information.")
        print("Please include a short report with what you did.")
        print()
        print("Place ID: " + fileID)
        print("Last ID: " + lastID)
        print()
        print("Error details:")
        sys.stderr.write(str(e) + "\n")
        print()
        print("Likely error cause: Initial description line length incorrect")
        input("Press enter to continue\n")
        cont = False
    except Exception as e:
        print()
        sys.stderr.write("An error has ocurred.\n")
        print()
        print("Please contact the game maker with the place ID.")
        print("Please include a short report with what you did.")
        print("Error details:")
        sys.stderr.write(str(e) + "\n")
        input("Press enter to continue\n")
        cont = False
        
