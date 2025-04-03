def bellman_ford(graph, start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0

    for _ in range(len(graph)):
        for i in graph:
            for edge, weight in graph[i]:
                if dist[i] + weight < dist[edge]:
                    dist[edge] = dist[i] + weight
    for i in graph:
        for edge, weight in graph[i]:
           if dist[i] + weight < dist[edge]:
               raise ValueError('neg weight cycle')

    return dist

graph = {
    0: [[1,4], [2,1]],
    1: [[3,1]],
    2: [[1,2],[3,5]],
    3: [[4,3]],
    4 : []
}
print(bellman_ford(graph, 0))



