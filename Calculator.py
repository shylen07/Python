i=1
while i<=4: 
    num1=int(input("Enter First number : "))
    num2=int(input("Enter Second number : "))
    operation=input("Enter Operation : ")
    if operation == "+":
        print(num1+num2)
    elif operation == "*":
        print(num1*num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "/":
        print(num1/num2)
    else:
        print("Invalid operation")
    i=i+1
