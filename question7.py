# program according to question  7
class student():
    pass
class Marks():
    pass
student_1=student()
Marks_1=Marks()
print("The instance student_1 is a instance of class student : ",isinstance(student_1,student))
print("The instance student_1 is a instance of class Marks : ",isinstance(student_1,Marks))
print("The instance Marks_1 is a instance of class student : ",isinstance(Marks_1,student))
print("The instance Marks_1 is a instance of class Marks : ",isinstance(Marks_1,Marks))
print("The class student is a sub-class of of the built in object class : ",issubclass(student,object))
print("The class Marks is a sub-class of of the built in object class : ",issubclass(Marks,object))