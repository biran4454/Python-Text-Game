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
"""
import sys
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
def eq(cmd, s):
    return(cmd.lower() == s.lower())

fileID = "1"
inventory = []
cont = True
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
                print(f.readline()[:-1])
            
            for i in range(int(f.readline())): #Add items to inventory
                inventory.append(f.readline()[:-1])
            
            choiceLen = int(f.readline()[:-1])
            for i in range(choiceLen): #Populate possible choices
                choices.append(f.readline()[:-1].lower())
                choiceIsDoor.append(f.readline()[:-1] == "Door")
                choiceIDs.append(f.readline()[:-1])
                choiceReq.append(f.readline()[:-1])
                choiceReqShown.append(f.readline()[:-1])
                choiceSel.append(f.readline()[:-1])
                choiceDie.append(f.readline()[:-1])
            print()
            print("Enter command")
            isNextDoor = False
            nextDoor = -1
            while not isNextDoor:
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
                                if(choiceIsDoor[moveChoice]): #If its a door open it
                                    nextDoor = choiceIDs[moveChoice]
                                    isNextDoor = True
                                    print(choiceSel[moveChoice])
                                    input("Press enter to continue...\n")
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
                        
            
            
            fileID = choiceIDs[moveChoice]
    except Exception as e:
        sys.stderr.write("An error has ocurred.\n")
        print("")
        print("Please contact the game maker with the place ID.")
        print("Please include a short report with what you did.")
        print("Error details:")
        sys.stderr.write(str(e) + "\n")
        input("Press enter to continue\n")
        cont = False
        
