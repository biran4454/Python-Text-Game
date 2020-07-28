import save
import sys
import random
import enemy
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


fileID = input("Enter starting point\n>>> ")
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
    inventory = save.gPlayerInventory()
    try:
        with open("FixedData\\Locations\\" + fileID + ".txt") as f:
            #PRINT LOCATION ID
            print("-- ID: " + fileID + " --\n")

            #PRINT STORY
            for i in range(int(f.readline()[:-1])):
                line = f.readline()
                if line[:-1] == "!break":
                    rprint("Press enter to continue... ")
                    input("")
                else:
                    if len(line[:-1]) > 0 and line[0] == "+":
                        rprint(line[1:])
                    else:
                        print(line[:-1])
            #ADD TO INVENTORY
            for i in range(int(f.readline())):
                inventory.append(f.readline()[:-1])

            #POPULATE CHOICES
            choiceLen = int(f.readline()[:-1])
            for i in range(choiceLen):
                choices.append(f.readline()[:-1].lower())
                choiceIsDoor.append(f.readline()[:-1] == "1")
                choiceIDs.append(f.readline()[:-1])
                choiceReq.append(f.readline()[:-1])
                choiceReqShown.append(f.readline()[:-1])
                choiceSel.append(f.readline()[:-1])
                choiceDie.append(f.readline()[:-1])
                choiceInvAdd.append(f.readline()[:-1])
            print()

            #FIND ENEMY
            isNextDoor = False
            nextDoor = -1
            if(f.readline()[:-1] == "True"): #If there's an enemy
                attackResult = enemy.loadEnemy(fileID) #Run attack sequence
                if(attackResult == 0): #And process the result
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
            #RUN COMMANDS
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
                    print(inventory)
                if eq(firstCmd, "exit") or eq(firstCmd, "quit"): #If first word is exit or quit
                    rprint("PRESS CANCEL IF IN PYSHELL\n")
                    exit("User selected exit game")
                if eq(firstCmd, "input"): #If the user wants to move
                    if(firstCmdIndex != -1):
                        secondCmdIndex = len(command)
                        secondCmd = command[firstCmdIndex + 1:secondCmdIndex].lower()
                        try:
                            moveChoice = choices.index(secondCmd)
                            if(choiceReq[moveChoice] == "" or inventory.count(choiceReq[moveChoice]) > 0): #If you have the right items
                                if(choiceDie[moveChoice] == "True"): #If the choice kills you
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
                            rprint("The command \"" + secondCmd + "\" doesn't exist!\n")
                    else:
                        rprint("You need to choose somewhere to move to!\n")
                
            save.sPlayerInventory(inventory)
            fileID = nextDoor
    except ValueError as e:
        print()
        rprint("An error has occurred.\n")
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
        rprint("An error has occurred.\n")
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
        rprint("An error has occurred.\n")
        print()
        print("Please contact the game maker with the place ID.")
        print("Please include a short report with what you did.")
        print("Error details:")
        rprint(str(e) + "\n")
        input("Press enter to continue\n")
        cont = False
