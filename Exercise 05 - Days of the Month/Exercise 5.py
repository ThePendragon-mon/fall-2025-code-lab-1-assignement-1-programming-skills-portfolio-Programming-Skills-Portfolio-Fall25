n=int(input("Enter the number of month: "))
if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12:
    print("There are 31 days in this month")
elif n==4 or n==6 or n==9 or n==11:
    print("There are 30 days in this month")
elif n==2:
    print("There are 28-29 days in Febuary")
else:
    print("I think you choose wrong number")
