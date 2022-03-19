# Python Text Game
 A text adventure game made in python.
 
 Each location is a file named `locationID.txt`.
 Use `input` to enter a command.
 Use `inventory` to see inventory.
 Use `Quit` and press cancel to exit.

## Notes
 Launch the python file via. idle because I'm too lazy to make it work without.

# Instructions
 The program runs via. a text command-like interface.
 The story will have capitalised letters for your options.
 Text in red is important.

 ## Commands
  After it has printed the story, if there is no creature to attack, it will ask you to "Enter command".
  At this point, you can type the following commands:

  Exit or quit: exit the program

  Inventory: view your charector's inventory (items)

  Input [option]: explained below.

 ## Input commands
  For the input option, you must type a command (written in capital letters in the story) after.
  E.g: input enter the cave
  You can usually write input back to go back to the previous place (possibly a few moves before depending on where you are)

  NOTE: Some input commands are hidden and not written in the story! These are secret commands that you have to look for. If you think of one that should be added, feel free to submit an issue.

 ## Attacking creatures
  If you come across an attacking creature, it will attack you, then you will attack it.
  Creatures have different attack amounts, health, and accuracies that make them range from easy to impossible to beat.
  When you come back to a room it will reset the creature and your health.
  Creatures may drop items when defeated.

  The attack command line goes like this:

  Enemy found: Snake

  It attacks, but misses

  You attack, but miss

  Your health:  ▅▅▅▅▅▅▅▅▅▅▅

  Enemy health: ▅▅

  Command? (Escape, Medi, Use, [enter])

  The first line tells you the enemy you are fighting.

  The second and third line tells you the result of the first attack.

  The fourth and fifth line tells you your health and your enemy's health in the form of a health bar.

  The sixth line asks you for a command.

 ## Attacking creatures commands
  Here are the attack commands:

  Escape: Go back to your previous location. Similar (but not the same) as input back.

  Medi: Use a medipack to restore your health.

  Use: Use an item in your inventory to allow a second attack on the creature.

  [enter]: Press the enter key to continue attacking.

  E.g: Use rocks
  E.g: Medi health pack
