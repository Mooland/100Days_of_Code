print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first_desicion=input("Are you going right or left?")
if first_desicion.lower()=="right":
    print("You fall into a hole. Game over")
else:
    print("You come to the nice beach")
    second_desicion=input("Will you swim to island or wait?")
    if second_desicion.lower()=="swim":
        print("You've been attacked by trout. Game over")
    else:
        print("You found a cavern with four doors: Red, Blue, Green and Yellow.")
        third_desicion=input("Which door will you pick?")
        if third_desicion.lower()=="red":
            print("You fall into lava. Game over")
        elif third_desicion.lower()=="blue":
            print("You've been eaten by bear. Game over")
        elif third_desicion.lower()=="yellow":
            print("You won!")
        else:
            print("You are dead. Game over")