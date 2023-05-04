import random

def get_random_string(length: int) -> str:
    result = ""
    for i in range(length):
        while True:
            code = random.randint(48, 122)
            if chr(code).isdigit() or chr(code).isalpha():
                result += chr(code)
                break
    return result
print(get_random_string(22))
