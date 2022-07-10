#program to check if a string is a palindrome or not
def palindrome():
    str = input("Enter a word to check whether it is palindrome or not : ")
    str = str.lower()
    str_rev = str[::-1]
    if(str==str_rev):
        print("The word is palindrome.")
    else:
        print("The word is not palindrome.")
palindrome()
