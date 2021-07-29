import algoritmos as ALG
import sys

n_cases = int(input())

for case in range(n_cases):
    [n, m, S, T] = [int(k) for k in input().split()]
    adjacency_matrix = [[sys.maxsize for columna in range(n)] for fila in range(n)]
    answer1 = sys.maxsize
    answer2 = sys.maxsize
    
    if (n > 1 and m > 0):
    	for k in range(m):
	        [server1, server2, latency] =  [int(p) for p in input().split()]

	        adjacency_matrix[server1][server2] = latency
        	adjacency_matrix[server2][server1] = latency
    
    	
    	answer1 = ALG.dijkstra(n, T, adjacency_matrix)[S]
    
    	answer2 = ALG.floyd_warshall(n, adjacency_matrix)[S][T]    
            
    if  (answer1 == sys.maxsize and answer2 == sys.maxsize):
        print("unreachable")
    else:
        print("Case #", case+1, ":")
        print("Segun Dijkstra:\t", answer1)
        print("Segun Floyd Warshall:\t", answer2)