import random

def get_random_string(length: int) -> str:
    result = ""
    for i in range(length):
        if i % 3 == 0:
            result += chr(random.randint(65, 90 if random.random() > 0.5 else 122))
        elif i % 3 == 1:
            result += chr(random.randint(48, 57))
        else:
            result += chr(random.randint(97, 122))
    return result
print(get_random_string(10))
