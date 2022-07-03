#program to sort a list into alphabetical order
def list_sort():
    str = input("Enter the string with hyphen separated sequence to arrange it in alphabetical order : ")
    words = str.split("-")
    words = sorted(words)
    for i in words:
        print(i, "\b-", end="")
    print("\b ")
list_sort()