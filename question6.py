# program to create a given function
def student_data(student_name="N.A.",student_class="N.A"):
    global student_id
    print("### Data Print ###")
    print("Student ID : ",student_id)
    if(student_name!="N.A."):
        print("Student Name : ",student_name)
    if(student_class!="N.A."):
        print("Student Class : ",student_class)
student_id=input("Enter the Student ID : ")
cond=input("If you want to enter only student name then press n, only student class then c or both then b : ")
if(cond=="n"):
    s_name=input("Enter the Student's Name : ")
    student_data(s_name)
elif(cond=="c"):
    s_class=input("Enter the Student's class : ")
    student_data(s_class)
elif(cond=="b"):
    s_name=input("Enter the Student's Name : ")
    s_class=input("Enter the Student's class : ")
    student_data(s_name,s_class)
else:
    student_data()