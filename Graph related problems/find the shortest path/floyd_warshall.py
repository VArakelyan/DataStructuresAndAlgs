def floyd_warshall(graph):
    n = len(graph)
    dist = []
    for i in range(n):
        dist.append([])
        for j in range(n):
            dist[i].append(graph[i][j])


    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


graph = [
    [0, 3, float('inf'), 5],
    [2, 0, float('inf'), 4],
    [float('inf'), 1, 0, float('inf')],
    [float('inf'), float('inf'), 2, 0]
]

shortest_paths = floyd_warshall(graph)
print(shortest_paths)


