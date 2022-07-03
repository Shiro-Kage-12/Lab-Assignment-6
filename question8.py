# program to find the three elements that sum to zero from a set of n real numbers
class sum():
    def __init__(self,list):
        self.list=list
    def py_1(self):
        l1=len(self.list)
        print(self.list)
        sum_list=[]
        for i in range(0,l1-2):
            for j in range(i+1,l1-1):
                for k in range(j+1,l1):
                    sum=self.list[i]+self.list[j]+self.list[k]
                    if(sum==0):
                        sum_list.append([self.list[i],self.list[j],self.list[k]])
        return sum_list
list=[int(item) for item in input("Enter the numbers : ").split(",")]
a=sum(list)
print("The numbers which makes the sum equal to 0 are : ",a.py_1())