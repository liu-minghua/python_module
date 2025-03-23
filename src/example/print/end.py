# Demonstrating the use of the 'end' argument in the print function, including no newline
# character, and a custom character.
# The 'end' argument is used to specify what character should be printed at the end of the line.
# By default, the 'end' argument is set to '\n' which means that a newline character will be printed    at the end of the line.
# If you want to print something else at the end of the line, you can specify it using the 'end' argument.  
# remove the newline character at the end of the line

def end_demo():
    print("Hello", end=" ")
    print("World")

    print("This is", end="-")
    print("a test")
    print("This is", end="*")
    print("a demo")

    for i in range(1, 11):
        if i == 10:
            print(i)
        print(i, end=" ")