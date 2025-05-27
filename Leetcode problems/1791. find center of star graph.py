def center(edges):
    a, b = edges[0]
    c, d = edges[1]
    if a == c or a == d:
        return a
    else:
        return b

edges = [[1,2],[5,1],[1,3],[1,4]]
print(center(edges))