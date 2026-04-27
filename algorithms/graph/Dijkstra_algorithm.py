import heapq

class Edge:
    def __init__(self, weight, start, target): # the algorithm works for directed graphs, so each edge has a start and a target
        self.weight = weight
        self.start = start
        self.target = target

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbour = []
        self.distance = float('inf')

    def __lt__(self, other):
        return self.distance < other.distance

    def add_edge(self, weight, destination):
        edge = Edge(weight, self, destination)
        self.neighbour.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start):
        start.distance = 0
        heapq.heappush(self.heap, start)
        while self.heap:
            # pop element with the lowest distance
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            # consider the neighbors:
            for edge in actual_vertex.neighbour:
                src = edge.start
                dst = edge.target
                new_dist = src.distance + edge.weight
                if new_dist < dst.distance:
                    dst.distance = new_dist
                    dst.predecessor = src
                    # update the heap
                    heapq.heappush(self.heap, dst)
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f'The shortest path to the vertex is {vertex.distance}')
        while vertex is not None:
            print(vertex.name, end=' ')
            vertex = vertex.predecessor

