import art
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

def calculator():
    print(art.logo)
    asking =True
    result=float()
    first_no = float(input("what is the first number: "))
    while asking:

        print("+\n-\n*\n/")
        operation = input("Pick an Operation: ")
        second_no=float(input("what is the next number: "))

        if operation=="+":
            result= float(round(add(first_no,second_no),2))
            print(f"{first_no} + {second_no} = {result}")

        elif operation=="-":
            result=float(round(subtract(first_no,second_no),2))
            print(f"{first_no} - {second_no} = {result}")

        elif operation=="*":
            result=float(round(multiply(first_no,second_no),2))
            print(f"{first_no} * {second_no} = {result}")

        elif operation=="/":
            result=float(round(divide(first_no,second_no),2))
            print(f"{first_no} / {second_no} = {result}")
        else:
            print("Please Enter the Correct operation!")

        again=input(f"Type 'y' to continue with {result}, or type 'n' to start with new calculation: ")
        if again=="y":
            first_no=result

        elif again=="n":
            print("\n"*20)
            calculator()

calculator()
