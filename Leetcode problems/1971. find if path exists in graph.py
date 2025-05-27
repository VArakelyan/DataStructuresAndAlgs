def path_exists(n, edges, source, destination):
    graph = [[] for _ in range(n)]
    visited = [0] * n

    def dfs(node):
        if node == destination:
            return True
        visited[node] = True
        for neighbour in graph[node]:
            if not visited[neighbour]:
                if dfs(neighbour):
                    return True
        return False

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    return dfs(source)

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

print(path_exists(n, edges, source, destination))