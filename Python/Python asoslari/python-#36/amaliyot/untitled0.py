# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:11:37 2026

@author: ids
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def count(self):
        count = 0          # 0 dan boshla
        element = self.head
        while element:     # element None bo'lgunga qadar
            count += 1
            element = element.next
        return count
            
    def find_max(self):
        if self.head:
            katta = self.head
        else:
            print("List bo'sh")
            return

        element = self.head
        while element:
            if element.data > katta.data:
                katta = element
            element = element.next

        return katta.data
    
    def reverse(self):
        prev = None           # ✅ prev = None dan boshlanadi
        current = self.head   # ✅ current = birinchi node

        while current:
            next_node = current.next  # keyingini saqla
            current.next = prev       # orqaga ko'rsat
            prev = current            # prev ni siljit
            current = next_node       # current ni siljit

        self.head = prev      # ✅ yangi head = oxirgi node

    def delete(self, value):
        # Head larni o'chir
        while self.head and self.head.data == value:
            self.head = self.head.next

        # Qolganlarini o'chir
        prev = self.head
        current = self.head.next
        while current:
            if current.data == value:
                prev.next = current.next  # o'chir
            else:
                prev = current            # siljit
            current = current.next

    def find_middle_oddiy(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next

        current = self.head
        for i in range(count//2):
            current = current.next
        return current.data



            
                
