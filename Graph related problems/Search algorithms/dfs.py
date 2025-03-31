from collections import deque

# Graph adjacency list
graph = {
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

def dfs(graph, start):
    stack = deque([start])
    visited = set([start])

    while stack:
        node = stack.pop()
        print(node, end=' ')

        # Iterate over neighbors in reverse to maintain the original order
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)


dfs(graph, 0)
