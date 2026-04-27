import sys

class Graph:
    def __init__(self,vertexnum, edges, nodes):
        self.vertexnum = vertexnum
        self.edges = edges
        self.nodes = nodes
        self.mst=[]

    def print_graph(self):
        print("Edge: Weight")
        for s, d, w in self.mst:
            print(f"{s} -> {d} : {w}")

    def primAlgo(self):
        visited = [False] * self.vertexnum
        visited[0] = True
        edge_count = 0
        while edge_count < self.vertexnum - 1:
            minimum = sys.maxsize
            s = -1
            d = -1
            for i in range(self.vertexnum):
                if visited[i]:
                    for j in range(self.vertexnum):
                        if not visited[j] and self.edges[i][j]:
                            if self.edges[i][j] < minimum:
                                minimum = self.edges[i][j]
                                s = i
                                d = j
            self.mst.append((self.nodes[s],self.nodes[d],self.edges[s][d]))
            visited[d] = True
            edge_count += 1
