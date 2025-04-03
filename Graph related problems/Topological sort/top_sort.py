
def dfs2(at, visited, visitednodes, graph):
    visited[at] = True
    neighbours = graph[at]
    for i in neighbours:
        if not visited[i]:
            dfs2(i, visited, visitednodes, graph)
    visitednodes.append(at)


def topsort2(graph):
    N = len(graph)
    visited = [False] * N
    result = []


    for at in graph:
        if not visited[at]:
            visitednodes = []
            dfs2(at, visited, visitednodes, graph)
            for v in visitednodes:
                result.append(v)

    return result


def topsort(graph):
    visited = [False] * len(graph)
    stack = []
    def dfs(at):
        visited[at] = True
        for neighbour in graph[at]:
            if not visited[neighbour]:
                dfs(neighbour)
        stack.append(at)

    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)
    return stack[::-1]


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
print(ord)
ord2 = topsort(graph)
print(ord2)