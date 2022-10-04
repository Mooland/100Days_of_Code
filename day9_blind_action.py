import course_art
import os

print(course_art.auction_logo)

print ("Welcome to the secret auction programm")

def clear():
    os.system('cls')

others_participants="yes"
bids={}
only_bids=[]
while others_participants=="yes":
    name=input("What is your name?: ")
    price=int(input("What is your bid?: $"))
    others_participants=input("Are there any other bidders? Type 'yes or 'no'. ")
    bids[name]=price
    clear()
    
print(f"And the winner is {max(bids, key=bids.get)}")


            

