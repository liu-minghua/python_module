from src.example.functions import times, divide
from src.example.string.string_functions import reverse
from src.module1 import add
def main():
    result = divide(times(3, 10), 5)
    print("3 times 10 divide 5 equals = ", result)
    prayer = "abracadabra"
    print("reverse of prayer is: ", reverse(prayer))
    print("Program is done.")

main()