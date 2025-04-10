from queue import Queue

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['J'],
    'C': ['F', 'I'],
    'D': ['G', 'E'],
    'E': ['K', 'H'],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': []
}
def kahns_algorithm(graph):
    n = len(graph)
    in_degree = {node: 0 for node in graph}

    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    q = Queue()
    for i in in_degree:
        if in_degree[i] == 0:
            q.put(i)


    order = []
    while not q.empty():
        at = q.get()
        order.append(at)
        for j in graph[at]:
            in_degree[j] -= 1
            if in_degree[j] == 0:
                q.put(j)


    if len(order) != n:
        return -1


    return order
print(kahns_algorithm(graph))
