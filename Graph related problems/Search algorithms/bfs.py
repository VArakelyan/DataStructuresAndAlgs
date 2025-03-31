from queue import Queue

g = {
    0: [7, 9, 11],
    1: [],
    2: [],
    3: [2, 4],
    4: [],
    5: [],
    6: [5],
    7: [6, 3, 11],
    8: [1, 12],
    9: [8, 10, 0],
    10: [1],
    11: [],
    12: [2]
}

def solve(s, graph):
    q = Queue()
    q.put(s)

    visited = {node: False for node in graph}
    visited[s] = True
    prev = {node: None for node in graph}

    while not q.empty():
        node = q.get()
        # Explore neighbors of the current node
        for neighbor in graph.get(node, []):
            if not visited[neighbor]:
                q.put(neighbor)
                visited[neighbor] = True
                prev[neighbor] = node
    return prev

def rec_path(s, e, prev):
    path = []
    at = e
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()

    # Check if the path starts with the source node
    if path[0] == s:
        return path
    return []

def bfs(s, e, graph):
    prev = solve(s, graph)
    return rec_path(s, e, prev)

print(bfs(0, 4, g))

