n=int(input("Enter the percentage : "))
if n>90:
    print("Grade : A")
elif n>80 and n<=90:
    print("Grade : B")
elif n>=60 and n<=80:
    print(*"Grade : B")
else:
    print("Grade : D")