import course_art

print (course_art.calculator_logo)




def multiply(a,b):
    return a*b

def plus(a,b):
    return a + b

def minus(a,b):
    return a - b

def division(a,b):
    return a*b

def calculator():
    keep_calc=True
    first_number=float(input("What's the first number?: "))
    operations={"+":plus,"-":minus,"/":division,"*":multiply}

    while keep_calc:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("Pick an operation: ")
        second_number=float(input("What's the second number?: "))
        
        answer=operations[operation_symbol](first_number,second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        if input(f"Type 'y' to continue operation with {answer}: ")=='y':
            first_number=answer
        else:
            should_continue=False
            calculator()
calculator()