from algorithms.graph import Floyd_Warshall_algorithm
from algorithms.graph import Dijkstra_algorithm
from algorithms.graph import check_route
from algorithms.graph import Prim_Algorithm

### -------------------
### Check Route Tests
### -------------------

def build_graph():
    customDict = {
        "a": ["c", "d", "b"],
        "b": ["j"],
        "c": ["g"],
        "d": ["a"],
        "e": ["f", "a"],
        "f": ["i"],
        "g": ["d", "h"],
        "h": [],
        "i": [],
        "j": []
    }
    return check_route.Graph(customDict)

def test_check_route_all():
    graph = build_graph()
    # direct
    assert graph.checkRoute("g", "h") is True
    assert graph.checkRoute("b", "j") is True
    # no path
    assert graph.checkRoute("h", "a") is False
    assert graph.checkRoute("i", "j") is False
    # cycle handling
    assert graph.checkRoute("a", "h") is True
    # bfs version
    assert graph.checkRouteQ("g", "h") is True
    assert graph.checkRouteQ("h", "a") is False
    # self node
    assert graph.checkRoute("a", "a") is True
    assert graph.checkRouteQ("a", "a") is True
    print("Check Route: all tests passed ✅")


### -------------------
### Dijkstra Tests
### -------------------

def build_weighted_graph():
    nodeA = Dijkstra_algorithm.Node('A')
    nodeB = Dijkstra_algorithm.Node('B')
    nodeC = Dijkstra_algorithm.Node('C')
    nodeD = Dijkstra_algorithm.Node('D')
    nodeE = Dijkstra_algorithm.Node('E')
    nodeF = Dijkstra_algorithm.Node('F')
    nodeG = Dijkstra_algorithm.Node('G')
    nodeH = Dijkstra_algorithm.Node('H')
    nodeA.add_edge(6, nodeB)
    nodeA.add_edge(10, nodeC)
    nodeA.add_edge(9, nodeD)
    nodeB.add_edge(5, nodeD)
    nodeB.add_edge(16, nodeE)
    nodeB.add_edge(13, nodeF)
    nodeC.add_edge(6, nodeD)
    nodeC.add_edge(5, nodeH)
    nodeC.add_edge(21, nodeG)
    nodeD.add_edge(8, nodeF)
    nodeD.add_edge(7, nodeH)
    nodeE.add_edge(10, nodeG)
    nodeF.add_edge(4, nodeE)
    nodeF.add_edge(12, nodeG)
    nodeH.add_edge(2, nodeF)
    nodeH.add_edge(14, nodeG)
    return nodeA, nodeF

def test_dijkstra():
    start, target = build_weighted_graph()
    algorithm = Dijkstra_algorithm.Dijkstra()
    algorithm.calculate(start)
    # adjust depending on your implementation
    assert target.distance == 17
    print("Dijkstra: all tests passed ✅")

### -------------------
### Floyd-Warshall Tests
### -------------------

def test_floyd_warshall():
    graph = [
        [0, 8, float('inf'), 1],
        [float('inf'), 0, 1, float('inf')],
        [4, float('inf'), 0, float('inf')],
        [float('inf'), 2, 9, 0]
    ]
    result = Floyd_Warshall_algorithm.floyd_warshall_algorithm(graph)
    assert result[0][2] == 4
    assert result[3][0] == 7
    print("Floyd-Warshall: all tests passed ✅")

def test_Prim():
    edges = [[0,10,20,0,0],
               [10,0,30,5,0],
               [20,30,0,15,6],
               [0,5,15,0,8],
               [0,0,6,8,0]]
    nodes = ["a","b","c","d","e"]
    g = Prim_Algorithm.Graph(5,edges,nodes)
    g.primAlgo()
    g.print_graph()

test_check_route_all()
test_dijkstra()
test_floyd_warshall()
test_Prim()