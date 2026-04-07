from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1) # Yo'naltirilmagan bo'lgani uchun

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")

# BFS (Eniga qidirish)
    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        print("BFS tartibi:", end=" ")
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

    # DFS (Bo'yiga qidirish - Rekursiv usulda)
    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
            print("DFS tartibi:", end=" ")
        
        visited.add(vertex)
        print(vertex, end=" ")
        
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Grafni yaratish
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")

g.add_edge("A", "B")
g.add_edge("A", "C")

g.print_graph()

print(g.bfs("A"))