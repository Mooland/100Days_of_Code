
import random
import course_art
import hangman_words

stages = course_art.stages

word_list = hangman_words.word_list

chosen_word=random.choice(word_list)

display=[]
for item in chosen_word:
    display.append("_")

game_is_on=0

lifes=6
input_tracker=[]
print(course_art.hangman_logo)
while game_is_on==0:
    print(stages[lifes])
    print(display)

    guess=input("Guess a letter in word: ").lower()
    
    if  guess in input_tracker:
            print(f"Hey you've tried '{guess}' letter before")
    else:
        input_tracker.append(guess)

    #checking if input present in chosen_word
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
        else:
            pass
    #game logic below:
    if guess not in chosen_word:
        lifes-=1        
        print(f"Sad, but '{guess}' not in the word")
    
    
    if "".join(display)==chosen_word:
        game_is_on=1
        print("You won")

    elif lifes==0:
        game_is_on=1
        print(stages[0])
        print("You lost")
    else:
        pass
    
