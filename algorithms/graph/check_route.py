from collections import deque

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def checkRoute(self, start_node, end_node, visited=None):
        if visited is None:
            visited = set()
        if start_node == end_node:
            return True
        visited.add(start_node)
        for neighbor in self.gdict.get(start_node, []):
            if neighbor not in visited: # makes sure you are not going in circles
                if self.checkRoute(neighbor, end_node, visited):
                    return True
        return False

    def checkRouteQ(self, start_node, end_node):
        visited = {start_node}
        queue = deque([start_node])
        while queue:
            node = queue.popleft()
            for neighbor in self.gdict.get(node, []):
                if neighbor == end_node:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

