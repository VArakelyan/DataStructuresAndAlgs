def factorial_dp(n, memo=[1]):

    if n < len(memo):
        return memo[n]

    for i in range(len(memo), n + 1):
        memo.append(i * memo[i - 1])

    return memo[n]

print(factorial_dp(5))
print(factorial_dp(4))
print(factorial_dp(6))