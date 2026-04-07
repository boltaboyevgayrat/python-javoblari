import random as r
def user_name(ism):
    return f"{ism[::-1]}{r.randint(0,9)}"

def convert_add(numbers):
    return sum([int(num) for num in numbers])


print(convert_add(["1", "2", "3"]))


    