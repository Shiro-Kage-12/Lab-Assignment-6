# program to check whether a string is a pangram or not
def pangram():
    sen = input("Enter the sentence to check whether it is panagram or not: ")
    a = 97
    A = 65
    count = 0
    for i in range(1, 27):
        for i in range(0, len(sen)):
            if (sen[i] == chr(a) or sen[i] == chr(A)):
                count += 1
                break
        a = a + 1
        A = A + 1
    if (count == 26):
        print("The sentence is pangram.")
    else:
        print("The sentence is not pangram.")
pangram()
