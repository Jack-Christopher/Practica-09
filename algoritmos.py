import sys

##############################################################
################### ALGORITMO DIJKSTRA #######################
##############################################################

def distanciaMinima(n_vertices, dist, visited_elements):
    minimo = sys.maxsize
    for v in range(n_vertices):
        if dist[v] < minimo and (not visited_elements[v]):
            minimo = dist[v]
            min_index = v
    return min_index

def dijkstra(n_vertices, inicio, graph):
    dist = [sys.maxsize] * n_vertices
    dist[inicio] = 0
    visited_elements = [False] * n_vertices
    for k in range(n_vertices):
        u = distanciaMinima(n_vertices, dist, visited_elements)
        visited_elements[u] = True
        for v in range(n_vertices):
            if graph[u][v] > 0 and (not visited_elements[v]) and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    return dist


##############################################################
############### ALGORITMO FLOYD - WARSHALL ###################
##############################################################

def floyd_warshall(n_vertices, graph):
    dist = graph
    for k in range(n_vertices):
        for i in range(n_vertices):
            for j in range(n_vertices):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j] )
    return dist
