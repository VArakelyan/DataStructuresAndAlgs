def fibonacci(n, memo=[0, 1]):
    if n < len(memo):
        return memo[n]

    for i in range(len(memo), n + 1):
        memo.append(memo[i - 1] + memo[i - 2])

    return memo[n]

print(fibonacci(6))
print(fibonacci(4))
print(fibonacci(7))