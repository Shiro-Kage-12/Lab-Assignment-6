# program to find the perfect number
def perfect_num():
    n=int(input("Enter a number to find if it is a perfect number or not : "))
    check=0
    for i in range(1,int(n/2)+1):
        if(n%i==0):
            check=check+i
    if(n==check):
        print("The number is a perfect number.")
    else:
        print("The number is not a perfect number.")
perfect_num()
