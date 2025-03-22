from src.example.functions import times, divide
from src.example.string.string_functions import reverse
from src.module1 import add
def main():
    result: float = divide(times(3, 10), 5)
    print("3 times 10 divide 5 = ", result)
    result: float = add(result, 100)
    print("add 100 to the result = ", result)
    prayer: str = "abracadabra"
    print("prayer is: ", prayer)
    print("reverse of prayer is: ", reverse(prayer))
    print("Program is done.")

main()