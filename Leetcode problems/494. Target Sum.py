def target_sum(elems, target):
    total = sum(elems)
    if total < abs(target) or (total + target) % 2 != 0:
        return 0
    s = (total + target) // 2
    memo = [0] * (s + 1)
    memo[0] = 1
    for elem in elems:
        for j in range(s, elem - 1, -1):
            memo[j] += memo[j - elem]
    return memo[s]


elems = [1,1,1,1]
target = 2
print(target_sum(elems, target))
