import algoritmos as ALG
import sys

n_cases = int(input())
for k in range(n_cases):
    input()
    N = int(input())
    E = int(input())
    T = int(input())
    M = int(input())
    adjacency_matrix = [[sys.maxsize for column in range(N)] for row in range(N)]
    for connection in range(M):
        temp = [int(k) for k in input().split()]  # a, b , t
        adjacency_matrix[temp[0]-1][temp[1]-1] = temp[2]

    # DIJKSTRA
    
    result = ALG.dijkstra(N, E, adjacency_matrix)
    total = 0
    for node in range(N):
        if result[node] <= T:
            total += 1
    print("Segun Dijkstra:\t", total)
    
    result2 = ALG.floyd_warshall(N, adjacency_matrix)
    total = 1
    for node in range(N):
    	if (result2[node][E] <= T) and (node != E):
    		total += 1 
    print("Segun Floyd Warshall:\t", total)




