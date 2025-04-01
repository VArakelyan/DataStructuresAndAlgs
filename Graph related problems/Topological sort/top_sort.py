
def dfs(at, visited, visitednodes, graph):
    visited[at] = True
    neighbours = graph[at]
    for i in neighbours:
        if not visited[i]:
            dfs(i, visited, visitednodes, graph)
    visitednodes.append(at)


def topsort(graph):
    N = len(graph)
    visited = [False] * N
    result = []


    for at in graph:
        if not visited[at]:
            visitednodes = []
            dfs(at, visited, visitednodes, graph)
            for v in visitednodes:
                result.append(v)

    return result

graph = {
    0: [3],
    1: [3],
    2: [0,1],
    3: [6, 7],
    4: [0, 3, 5],
    5: [9, 10],
    6: [8],
    7: [8, 9],
    8: [11],
    9: [11, 12],
    10: [9],
    11: [],
    12: []
}


ord = topsort(graph)
ord.reverse()
print(ord)
