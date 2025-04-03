# we use topological sort to ensure when we check the
# distance for current node, we have checked all previous connections


def topsort(graph):
    visited = [False] * len(graph)
    stack = []
    def dfs(at):
        visited[at] = True
        for neighbour in graph[at]:
            node = neighbour[0]
            if not visited[node]:
                dfs(node)
        stack.append(at)

    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)
    return stack[::-1]


def longest_path(graph, start):
    top_order = topsort(graph)
    dist = [-float('inf')] * len(graph)
    dist[start] = 0

    for i in (top_order):
        if dist[i] != -float('inf'):
            for edge, weight in graph[i]:
                if dist[edge] < dist[i] + weight:
                    dist[edge] = dist[i] + weight
    return dist


graph = {
    0: [[1,4], [2,1]],
    1: [[3,1]],
    2: [[1,2],[3,5]],
    3: [[4,3]],
    4 : []
}

start = 0
print(longest_path(graph, start))