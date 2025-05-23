def knapsack(v, w, c):
    n = len(w)
    memo = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, c + 1):

            if w[i - 1] <= j:
                memo[i][j] = max(memo[i-1][j], v[i-1] + memo[i-1][j - w[i-1]])
            else:
                memo[i][j] = memo[i-1][j]
    return memo[n][c]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

result = knapsack(values,weights, capacity)
print(result)
