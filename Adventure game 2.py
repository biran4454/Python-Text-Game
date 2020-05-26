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
Choice select text #1
Does door kill you? #1
Door item drop #1
Is there an enemy?
Enemy name
Enemy attack
Enemy health
Enemy accuracy
Enemy item drops
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
def rprint(text):
    sys.stderr.write(text)

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
            for i in range(int(f.readline()) * 8):
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
                        print("▅", end="")
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
                attackCmd = input("Command? (Escape, Continue, Medi, Use)\n>>> ").lower()
                try:
                    firstCmdIndex = attackCmd.index(' ') #Get first word
                except ValueError:
                    firstCmdIndex = len(attackCmd)
                firstCmd = attackCmd[:firstCmdIndex].lower()
                
                if(firstCmd == "escape"):
                    return(2)
                if(firstCmd == "medi"):
                    if(inventory.count("medipack") > 0 or inventory.count("Medipack") > 0):
                        playerHealth += 20
                        playerHealth = min(playerHealth, 60)
                if(firstCmd == "use"):
                    if(firstCmdIndex != -1):
                        secondCmdIndex = len(attackCmd)
                        secondCmd = attackCmd[firstCmdIndex + 1:secondCmdIndex].lower()
                        if(eq(secondCmd, "rocks")):
                            attackEnemy()
                        else:
                            rprint("You can't use " + secondCmd + ". \n")
                    else:
                        rprint("Nothing selected to use. Continuing.\n")
            
    except OSError:
        rprint("File does not exist. Please contact the program maker.\n")
        return(1)

def attackPlayer():
    result = random.randrange(10)
    if(result <= enemyAccuracy):
        effect = random.randrange(max(enemyAttack - 20, 4), max(enemyAttack, 6))
        result = random.randrange(10)
        rprint("It attacks and does " + str(effect) + " damage\n")
        return(effect)
    else:
        print("It attacks, but misses")
        return(0)

def attackEnemy():
    result = random.randrange(10)
    if(result <= playerAccuracy):
        effect = random.randrange(max(playerAttack - 20, 4), max(playerAttack, 6))
        result = random.randrange(10)
        rprint("You attack and do " + str(effect) + " damage\n")
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
    choiceInvAdd = []
    try:
        with open(fileID + ".txt") as f:
            print("-- ID: " + fileID + " --\n") #Print location ID
            
            for i in range(int(f.readline()[:-1])): #Print story background
                line = f.readline()
                if line[:-1] == "+break":
                    input("Press enter to continue... ")
                else:
                    if len(line[:-1]) > 0 and line[0] == "+":
                        rprint(line[1:])
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
                choiceInvAdd.append(f.readline()[:-1])
            print()
            isNextDoor = False
            nextDoor = -1
            if(f.readline()[:-1] == "True"):
                attackResult = loadEnemy(fileID)
                if(attackResult == 0):
                    rprint("You died.\n")
                    input("Press enter to continue...\n")
                    rprint("PRESS CANCEL IF IN PYSHELL\n")
                    exit("User died")
                    cont = False
                if(attackResult == 2):
                    isNextDoor = True
                    nextDoor = lastID
                    lastID = fileID
                else:
                    for i in range(4):
                        f.readline()[:-1]
                    drop = f.readline()[:-1]
                    if drop != "":
                        rprint("+ " + drop + "\n")
                        inventory.append(drop)
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
                    rprint("PRESS CANCEL IF IN PYSHELL\n")
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
                                    rprint("You died.\n")
                                    input("Press enter to continue...\n")
                                    rprint("PRESS CANCEL IF IN PYSHELL\n")
                                    exit("User died")
                                    cont = False
                                else:
                                    if(choiceIsDoor[moveChoice]): #If its a door open it
                                        nextDoor = choiceIDs[moveChoice]
                                        isNextDoor = True
                                        print(choiceSel[moveChoice])
                                        if(choiceInvAdd[moveChoice] != ""):
                                            rprint("+ " + choiceInvAdd[moveChoice] + "\n")
                                            inventory.append(choiceInvAdd[moveChoice])
                                        input("Press enter to continue...\n")
                                        lastID = fileID
                                    else:
                                        print(choiceSel[moveChoice]) #Otherwise just print the text
                                        if(choiceInvAdd[moveChoice] != ""):
                                            rprint("+ " + choiceInvAdd[moveChoice] + "\n")
                                            inventory.append(choiceInvAdd[moveChoice])
                            else:
                                if(choiceReqShown[moveChoice] == "True"):
                                    rprint("You need an item to do this: " + choiceReq[moveChoice] + "\n")
                                else:
                                    rprint("You can't do that now\n")
                        except ValueError:
                            rprint("The location \"" + secondCmd + "\" doesn't exist!\n")
                    else:
                        rprint("You need to choose somewhere to move to!\n")
                
            
            fileID = nextDoor
    except ValueError as e:
        print()
        rprint("An error has ocurred.\n")
        print()
        print("Please contact the game maker with the following information.")
        print("Please include a short report with what you did.")
        print()
        print("Place ID: " + fileID)
        print("Last ID: " + lastID)
        print()
        print("Error details:")
        rprint(str(e) + "\n")
        print()
        print("Likely error cause: Initial description line length incorrect")
        input("Press enter to continue\n")
        cont = False
    
    except FileNotFoundError as e:
        print()
        rprint("An error has ocurred.\n")
        print()
        print("Please contact the game maker with the following information.")
        print("Please include a short report with what you did.")
        print()
        print("Place ID: " + fileID)
        print("Last ID: " + lastID)
        print()
        print("Error details:")
        rprint(str(e) + "\n")
        print()
        print("Likely error cause: File missing, file name incorrect, or invalid file reference.")
        input("Press enter to continue\n")
        cont = False
    
    except Exception as e:
        print()
        rprint("An error has ocurred.\n")
        print()
        print("Please contact the game maker with the place ID.")
        print("Please include a short report with what you did.")
        print("Error details:")
        rprint(str(e) + "\n")
        input("Press enter to continue\n")
        cont = False
        
