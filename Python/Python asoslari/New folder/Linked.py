class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def lprint(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def push(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node
        
        
    def insertAfter(self, prev, new_data):
        if prev is None:
            print("Tugun mavjud emas.")
            return
        
        new_Node = Node(new_data)
        new_Node.next = prev.next
        prev.next = new_Node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        
        last = self.head
        while last.next:
            last = last.next
        
        last.next = new_node
        
    def deleteNode(self, key):
        temp = self.head
        
        if (temp and temp.data == key):
            self.head = temp.next
            temp = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return
        prev.next = temp.next
        temp = None
        