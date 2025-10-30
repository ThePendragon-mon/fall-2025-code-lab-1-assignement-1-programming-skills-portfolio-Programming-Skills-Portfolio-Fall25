def sol(num):
    if num%2==0:
        print("Number is even ")
    else:
        print("Number is odd ")
def main():
    n=int(input("Enter the number: "))
    r=sol(n)
    print(r)
if __name__=="__main__":
    main()
