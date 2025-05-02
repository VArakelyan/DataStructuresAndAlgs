def fac(n):
    returns = [0] * (n + 1)
    returns[0] = 1

    for i in range(1, n + 1):
        returns[i] = i * returns[i-1]

    return returns[n]


print(fac(5))