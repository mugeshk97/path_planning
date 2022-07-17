# # path planing using dijkstra algorithm

 
from queue import PriorityQueue

class Node(object):
    def __init__(self, name: str=None):
        self.name = name
        self.neighbour = []
        self.distance = float("inf")
        self.previous = None


    def __lt__(self, other):
        return self.name < other.name

    def __gt__(self, other):
        return self.name > other.name
        
    
    def add_neighbour(self, node, weight=1):
        edge = Edge(self, node, weight)
        self.neighbour.append(edge)            

    def __repr__(self):
        return f"{self.name} -> {self.neighbour}"
        
    
class Edge(object):
    def __init__(self, source: Node, destination: Node, weight: int=1):
        self.source = source
        self.destination = destination
        self.weight = weight
    
    def __repr__(self):
        return f"{self.destination.name} : {self.weight}"
  


S = Node('Start')
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
G = Node('End')

S.add_neighbour(A, 1)
S.add_neighbour(G, 12)

A.add_neighbour(B, 3)
A.add_neighbour(C, 1)

B.add_neighbour(D, 3)

C.add_neighbour(D, 1)
C.add_neighbour(G, 2)

D.add_neighbour(G, 3)


for node in [S, A, B, C, D, G]:
    print(node)


def dijkstra(source: Node, destination: Node):
    source.distance = 0
    q = PriorityQueue()
    q.put(source)
    while not q.empty():
        node = q.get()
        for edge in node.neighbour:
            if edge.destination.distance > edge.weight + node.distance:
                edge.destination.distance = edge.weight + node.distance
                q.put(edge.destination)
    print(f"Shortest path from {source.name} to {destination.name} is {destination.distance}")
    return destination.distance

print(dijkstra(S, G))
