# 4. Queue sinfini enqueue, dequeue, front, is_empty, size metodlari bilan amalga 
# oshirish. Navbat hosil qilish va barcha usullarning ishlashini ko‘rsatish.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.items)        
print(q.front())      
print(q.dequeue())  
print(q.items)       
print(q.size())       
print(q.is_empty())   
