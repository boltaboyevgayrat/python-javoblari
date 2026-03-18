# 1. Binar daraxt uchun elementlarni kiritish usullari va uchala aylanish turi 
# (to‘g‘ri, markaziy, teskari) mavjud bo‘lgan sinfni amalga oshirish.

class Tugun:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Tugun(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = Tugun(data)
            else:
                self._insert_recursive(current.left, data)
        else:
            if current.right is None:
                current.right = Tugun(data)
            else:
                self._insert_recursive(current.right, data)

    def pre_order(self, node):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def post_order(self, node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

bt = BinaryTree()
elements = [50, 30, 70, 20, 40, 60, 80]

for el in elements:
    bt.insert(el)

print("Pre-order (to'g'ri):")
bt.pre_order(bt.root)
print("\nIn-order (markaziy):")
bt.in_order(bt.root)
print("\nPost-order (teskari):")
bt.post_order(bt.root)

# ---------------------------------------------------------------------------------------------

# # 2. Binar qidiruv daraxtini yaratish va elementni qidirish usulini amalga oshirish. 
# # Minimal va maksimal elementlarni topish usullarini qo‘shish

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self):
#         self.root = None

#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert_recursive(self.root, data)

#     def _insert_recursive(self, current, data):
#         if data < current.data:
#             if current.left is None:
#                 current.left = Node(data)
#             else:
#                 self._insert_recursive(current.left, data)
#         elif data > current.data:
#             if current.right is None:
#                 current.right = Node(data)
#             else:
#                 self._insert_recursive(current.right, data)
#         # Agar data == current.data, uni qo'shmaymiz (uniq elementlar)

#     def search(self, data):
#         return self._search_recursive(self.root, data)

#     def _search_recursive(self, current, data):
#         if current is None:
#             return False  # Element topilmadi
#         if data == current.data:
#             return True   # Topildi
#         elif data < current.data:
#             return self._search_recursive(current.left, data)
#         else:
#             return self._search_recursive(current.right, data)
        
#     def find_min(self):
#         current = self.root
#         if not current:
#             return None
#         while current.left:
#             current = current.left
#         return current.data

#     def find_max(self):
#         current = self.root
#         if not current:
#             return None
#         while current.right:
#             current = current.right
#         return current.data
    
# bst = BST()
# elements = [50, 30, 70, 20, 40, 60, 80]

# for el in elements:
#     bst.insert(el)

# print("50 qidirilmoqda:", bst.search(50))
# print("25 qidirilmoqda:", bst.search(25))
# print("Minimal element:", bst.find_min())
# print("Maksimal element:", bst.find_max())