# 5. Stek yordamida o‘nli kasrni ikkili kasrga aylantiruvchi dastur tuzing. 

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


def decimal_to_binary(n):
    stack = Stack()

    while n > 0:
        qoldiq = n % 2
        stack.push(qoldiq)
        n = n // 2

    binary = ""

    while not stack.is_empty():
        binary += str(stack.pop())

    return binary


son = int(input("O‘nli son kiriting: "))
print("Ikkilik ko‘rinishi:", decimal_to_binary(son))
