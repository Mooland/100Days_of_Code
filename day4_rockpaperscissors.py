import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if player_input==0:
    print(rock)
elif player_input==1:
    print(paper)
else:
    print(scissors)

computer_pick=random.randint(0,2)
print("Computer chose:")
if computer_pick==0:
    print(rock)
elif computer_pick==1:
    print(paper)
else:
    print(scissors)

if player_input==computer_pick:
    print("It's a draw")
elif player_input>computer_pick or (player_input==0 and computer_pick==2):
    print("You won!")
else:
    print("You lost!")
