# 3. Matematik ifodada qavslarning (dumaloq, kvadrat va shakldor) to‘g‘ri 
# qo‘yilganligini tekshiruvchi funksiya tuzing.

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


def check_brackets(ifoda):
    stack = Stack()
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in ifoda:
        if char in "([{":
            stack.push(char)

        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != pairs[char]:
                return False

    return stack.is_empty()


ifoda = input("Ifoda kiriting: ")

if check_brackets(ifoda):
    print("Qavslar to‘g‘ri joylashtirilgan")
else:
    print("Qavslar noto‘g‘ri")

