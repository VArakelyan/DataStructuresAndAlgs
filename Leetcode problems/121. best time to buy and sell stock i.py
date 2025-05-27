def max_profit(a):
    min_ = float('inf')
    res = 0
    for x in a:
        if x < min_:
            min_ = x
        elif x - min_ > res:
            res = x - min_
    return res

prices = [7,1,5,3,6,4]
print(max_profit(prices))