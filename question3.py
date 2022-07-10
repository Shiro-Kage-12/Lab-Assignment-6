# program to print the first n rows of Pascal's triange
import math
def pascal_triangle():
    n=int(input("enter number of rows"))
    i=0
    space=n+2
    while(i<n):
        j=1
        while(j<=space):
            print(" ",end='')
            j+=1
        space-=1
        k=0
        while(k<i+1):
            output = math.factorial(i)//(math.factorial(k)*math.factorial(i-k))
            print(output,end=' ')
            k+=1
        i+=1
        print()
pascal_triangle()
