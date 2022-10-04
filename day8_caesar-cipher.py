import course_art

print (course_art.caesar_logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


user_want_to_continue='yes'




def caesar (text, shift,direction):
    if direction=="encode":
        print(f"The encoded text is {coder(text,shift)}")
    elif direction=='decode':
        print(f"The decoded text is {coder(text,-shift)}") #minus shift reverts number value to negative (works only if input number was positive)

def coder(text,shift):
    return_text=""
    for letter in text:
        if letter not in alphabet:
            return_text+=letter
        else:
            position=alphabet.index(letter)
            new_position=position + shift
            return_text+=alphabet[new_position]
    #print(return_text)
    return return_text

while user_want_to_continue=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>26:
        shift=shift%26
    else:
        pass
    print(caesar(text,shift,direction))
    user_want_to_continue=input("Do you want to continue? yes or no ")
print("Ciao")