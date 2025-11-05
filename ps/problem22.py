# function to prevent newline 

string = input("enter a string: ")
print(" this is printed in other line ")

# it isn't neccessary to check if string ends with \n
# since inpput doesn't include \n


def preventNewLine(string):
    print(string , end="")
    print(" this is printed in same line")

preventNewLine(string)
