# 1.	Push, pop, peek, is_empty va size usullari bilan Stack sinfini amalga oshirish. 
# Stek yaratish, unga 5 ta element qo‘shish va barcha usullarning ishlashini namoyish 
# etish.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack bo‘sh!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack bo‘sh!"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

print("Stack:", stack.items)

print("Elementlar soni:", stack.size())

print("Oxirgi element:", stack.peek())

print("O‘chirilgan element:", stack.pop())
print("Yangi stack:", stack.items)

print("Stack bo‘shmi:", stack.is_empty())

while not stack.is_empty():
    print("Pop:", stack.pop())

print("Oxirida stack bo‘shmi:", stack.is_empty())