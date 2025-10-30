n=0
n=int(input("Enter the password: "))
m=1
if n==12345:
    print("Welcome, User!")
else:
    while n!=12345 and m!=5:
        print("Wrong password! please try again!")
        n=int(input("Enter the password: "))
        m=m+1
        l=5-m
        if n!=12345:
            print(f"You have left {l} attempts")
    else:
        if n==12345:
            print("Welcome, User!")
        elif m==5:
            print("You've used all the attempts!")
        else:
            print("Unknown error")
