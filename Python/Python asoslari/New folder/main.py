from Linked import Node, LinkedList

llist = LinkedList()

llist.head = Node("Dushanba")
tuesday = Node("Seshanba")
wednesday = Node("Chorshanba")

llist.head.next = tuesday
tuesday.next = wednesday

llist.push("yakshanba")


