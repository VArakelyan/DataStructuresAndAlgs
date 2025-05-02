max_days = 50

c = 8

n = 4

m = 1

queries = [5]

initial_cows = [1,3,2,1]
dp = [[0 for _ in range(c + 1)] for _ in range(max_days + 1)]

def solve(c, n, m, queries, max_days, initial_cows):

    def sumRows(dp, day):
        farms = 0
        for i in range(c):
            farms += dp[day][i]
        return farms


    for i in range(n):
        dp[0][initial_cows[i]] += 1

    for day in range(max_days):
        for i in range(1, c):
            if i <= c/2:
                dp[day+1][2*i] += dp[day][i]
            else:
                dp[day+1][i] += 2 * dp[day][i]

    for i in range(m):
        day = queries[i]
        print(sumRows(dp, day))


solve(c, n, m, queries, max_days, initial_cows)

