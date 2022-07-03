# program to a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']
class check():
    def __init__(self,str):
        self.str=str

    def myfunc(self):
            count=0
            for i in range(0,len(self.str)):
                if(i%2!=0):
                    if(self.str[i-1]=="(" and self.str[i]==")"):
                        pass
                    elif(self.str[i-1]=="[" and self.str[i]=="]"):
                        pass
                    elif(self.str[i-1]=="{" and self.str[i]=="}"):
                        pass
                    else:
                        count+=1

            if(count==0):
                return "valid."
            else:
                return "invalid."
str=input("Enter the set of parenthesis to check whether it is valid or not : ")
a=check(str)
print("The set of parenthesis is ",a.myfunc())