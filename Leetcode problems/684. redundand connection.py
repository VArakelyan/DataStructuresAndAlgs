def redundant_connection(edges):

    save = [i for i in range(len(edges) + 1)]

    def f(x):
        if save[x] != x:
            save[x] = f(save[x])
        return save[x]

    def s(x, y):
        px = f(x)
        py = f(y)
        if px == py:
            return False
        save[px] = py
        return True

    for u, v in edges:
        if not s(u, v):
            return [u, v]


    return []


edges = [[1, 2],
         [1, 3],
         [2, 3]]
print(redundant_connection(edges))