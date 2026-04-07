class Node:
    def __init__(self, data):
        self.data = data  # Ma'lumot
        self.next = None  # Keyingi tugunga havola

class LinkedList:
    def __init__(self):
        self.head = None  # Ro'yxatning boshi

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:  # Oxirgi tugunni topish
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
            
        return False
    
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev
        
    def del_dublikate(self):
        current = self.head
        
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
                
    def get_middle(self):
        fast = self.head
        slow = self.head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow.data

# Ishlatib ko'ramiz:
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.append("E")
llist.append("F")
llist.append(("G"))
llist.append(("H"))
print(llist.search("d"))
print(llist.search("B"))


# llist.display()  # Natija: A -> B -> C -> None

# llist.reverse()
# llist.display()

# llist.del_dublikate()
# llist.display()

print(llist.get_middle())