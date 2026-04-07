class Stack:
    def __init__(self):
        self.items = []

    # element qo‘shish (push)
    def push(self, item):
        self.items.append(item)

    # element olib tashlash (pop)
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack bo'sh!")
        return self.items.pop()

    # oxirgi elementni ko‘rish (peek)
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack bo'sh!")
        return self.items[-1]

    # stack bo‘shligini tekshirish
    def is_empty(self):
        return len(self.items) == 0

    # stack o‘lchami
    def size(self):
        return len(self.items)

    # stackni chiqarish
    def display(self):
        return self.items
    
stack = Stack
stack.push(5)
stack.push(4)
stack.push(6)
stack.push(3)
stack.push(7)

