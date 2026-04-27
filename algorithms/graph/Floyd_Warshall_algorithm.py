def print_solution(distance_matrix):
    for row in distance_matrix:
        for col in row:
            if col == float('inf'):
                print("Infinity",end=" ")
            else:
                print(col,end=" ")
        print()

def floyd_warshall_algorithm(graph_f):
    n=len(graph_f)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph_f[i][k] != float('inf') and graph_f[k][j] != float('inf'):
                    graph_f[i][j]=min(graph_f[i][j],graph_f[i][k]+graph_f[k][j])
    return graph_f
