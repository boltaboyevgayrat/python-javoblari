# 2. Stek yordamida satrni teskari aylantiradigan dastur tuzish.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def reverse_string(text):
    stack = Stack()

    for char in text:
        stack.push(char)

    reversed_text = ""

    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text


matn = input("Matn kiriting: ")
print("Teskari matn:", reverse_string(matn))
