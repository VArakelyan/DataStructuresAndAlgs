
g = {
    0: [8],
    1: [5],
    2: [9],
    3: [9],
    4: [0],
    5: [16, 17],
    6: [11],
    7: [6],
    8: [4, 14],
    9: [15],
    10: [],
    11: [7],
    12: [],
    13: [0],
    14: [0, 13],
    15: [2, 10],
    16: [],
    17: []
}

n = len(g)
components = [0]*n
visited = [False]*n
count = 0

undirected_g = {i: [] for i in range(n)}
for node in g:
    for neighbor in g[node]:
        undirected_g[node].append(neighbor)
        undirected_g[neighbor].append(node)  # Add the reverse edge

def dfs(at):
    visited[at] = True
    components[at] = count
    for next_node in undirected_g[at]:
        if not visited[next_node]:
            dfs(next_node)


def find_components():
    global count
    for node in undirected_g:
        if not visited[node]:
           count += 1
           dfs(node)
    return count, components


res = find_components()
print(res)
