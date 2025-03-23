from src.example.functions import times, divide
from src.example.string.string_functions import reverse
from src.module1 import add
from src.example.print.sep import sep_demo
from src.example.print.end import end_demo
from src.example.print.fstring import fstring_demo
def main():
    result: float = divide(times(3, 10), 5)
    print("3 times 10 divide 5 = ", result)
    result: float = add(result, 100)
    print("add 100 to the result = ", result)
    prayer: str = "abracadabra"
    print("prayer is: ", prayer)
    print("reverse of prayer is: ", reverse(prayer))
    sep_demo()
    end_demo()
    name: str = "John"
    age: int = 30
    city: str = "New York"
    fstring_demo(name, age, city)
    print("Program is done.")

main()