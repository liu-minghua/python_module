# src/example/string/string_functions.py
def reverse(str: str)->str:
    result = ''
    for i in range(len(str)-1, -1, -1):
        result += str[i]
    return result