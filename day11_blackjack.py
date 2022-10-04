import imp
from multiprocessing import reduction
import random
import course_art
import os
#assuming that there are infinite amount of decks


#create random hands with two cards
#if pc hand has less <=16 - draw random card
#compare hands

def clear():
    os.system('cls')   

    
print(course_art.blackjack_logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    if len(hand)==2 and sum(hand)==21:
        return 0 #stands for blackjaclk
    for card in hand:
        if card==11 and sum(hand)>21:
            hand.remove(card)
            hand.append(1)

    return sum(hand)

def compare(userhand,computerhand):
    if calculate_score(userhand)==0 or calculate_score(computerhand)>21:
        print("You won!")
        return True
    elif calculate_score(computerhand)==0 or calculate_score(userhand)>21:
        print("You lost!")
        return True
    elif calculate_score(userhand)==calculate_score(computerhand):
        print("It;s a draw! ")
        return True
    elif calculate_score(computerhand)<calculate_score(userhand):
        print ("You won!")
        return True
    elif calculate_score(computerhand)>calculate_score(userhand):
        print("You lost! :(")
        return True
    else:
        return False

def game_bj():
    game_end=False
    while game_end==False:
        user_cards = []
        computer_cards = []

        user_cards.extend(random.choices(cards,k=2)) 
        computer_cards.extend(random.choices(cards,k=2))

        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer hand:{computer_cards[0]}")

        draw_another=input("Type 'y' to get another card, type 'n' to pass: ")

        while draw_another=="y":
            user_cards.append(deal_card())
            print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
            print(f"Computer hand:{computer_cards[0]}")
            draw_another=input("Type 'y' to get another card, type 'n' to pass: ")

        while calculate_score(computer_cards)<17:
            computer_cards.append(deal_card())
        print(f"Your cards: {user_cards}, final score: {sum(user_cards)}")
        print(f"Computer final hand:{computer_cards}, final score {sum(computer_cards)}")
        game_end=compare(userhand=user_cards,computerhand=computer_cards)

        another_round=input("Do you want to play another round? y or n: ")

        if another_round=='y':
            clear()
            print(course_art.blackjack_logo)
            game_bj()
        else:
            game_end=True
    
game_bj()

# def game_bj():
    
#     game_will=input("Do you want to play game of BlackJack? 'y' or 'n: ")
#     player_hand=[]
#     computer_hand=[]

#     while game_will=='y':
#         player_hand.extend(random.choices(cards,k=2)) 
#         computer_hand.extend(random.choices(cards,k=2))
#         print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
#         print(f"Computer first card:{computer_hand[0]}")

#         draw_another=input("Type 'y' to get another card, type 'n' to pass: ")
#         if draw_another=='y':
#             player_hand.extend(random.choices(cards,k=1))
#         elif draw_another=='n':
#             pass
           
#         if sum(computer_hand)<17:
#             computer_hand.extend(random.choices(cards,k=1))

#         print(f"Your cards: {player_hand}, final score: {sum(player_hand)}")
#         print(f"Computer final hand:{computer_hand}, final score {sum(computer_hand)}")

#         if sum(computer_hand)>sum(player_hand):
#             print("You lost :(")
#         elif sum(computer_hand)==sum(player_hand):
#             print("It's a draw!")
#         else:
#             print("You won!")
#         game_bj()
    
# game_bj()