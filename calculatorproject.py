
import os

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

operation_dict= {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division}


def calculator():

    num1=float(input("Enter the First Number:"))
    for symbol in operation_dict:

        print(symbol)

    continue_flag=True


    while continue_flag:

        operation_symbol=input("choose an operator:")  
        num2=float(input("Enter a Second Number:"))
        calculator_function=operation_dict[operation_symbol]
        output=calculator_function(num1,num2)

        print(num1, operation_symbol, num2, "=", output)

        should_continue=input("Enter 'x' to continue the previous calculation/ Enter 'y' to Perform new calculation/ Enter 'z' to EXIT ; ")

        if should_continue== 'x' or should_continue=='X':  

            num1=output  

        elif should_continue=='y' or should_continue=='Y':
            
             continue_flag==False
             os.system('cls')
             calculator()  

        elif should_continue == 'z'or should_continue=='Z':
             
             print("Goodbye!")

        else:

            print("Invalid input. Please enter 'x', 'y', or 'z'.")

calculator()




    