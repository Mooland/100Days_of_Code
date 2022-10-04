import random
import course_art


print(course_art.guess_number_logo)

game_is_on=True
while game_is_on==True:
    attempt_counter=10
    print("Welcome to the Number Guessing Game \nI'm thinking of a number between 1 and 100")
    guessed_number=random.randint(1,100)
    diffculty=input("Chose a diffculty. Type 'easy' or 'hard: '")
    if diffculty=='hard':
        attempt_counter=5
    print(f'You have {attempt_counter} attempts left.')
    while attempt_counter!=0:
        guess=int(input("Make a guess: "))
        if guess==guessed_number:
            print("You won!")
            break
        elif guess>guessed_number:
            print("Too high")
        elif guess<guessed_number:
            print("Too low")
        attempt_counter-=1
        print(f'You have {attempt_counter} attempts left.')
    game_is_on=False
