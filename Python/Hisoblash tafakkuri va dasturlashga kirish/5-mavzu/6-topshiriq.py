
# 6. Har bir mijoz buyurtma raqamiga ega bo‘lgan kafeda navbat simulyatsiyasini 
# yaratish. Dastur buyurtmalarni kelib tushish tartibiga qarab qayta ishlashi kerak.

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
    
kafe_navbat = Queue()

kafe_navbat.enqueue("Mijoz 1 - Buyurtma #101")
kafe_navbat.enqueue("Mijoz 2 - Buyurtma #102")
kafe_navbat.enqueue("Mijoz 3 - Buyurtma #103")
kafe_navbat.enqueue("Mijoz 4 - Buyurtma #104")

print("Navbatdagi mijozlar:")
print(kafe_navbat.items)

print("\nBuyurtmalarni qayta ishlash:")

while not kafe_navbat.is_empty():
    mijoz = kafe_navbat.dequeue()
    print(f"{mijoz} - buyurtma tayyorlandi")