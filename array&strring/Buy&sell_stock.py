prices=[7,1,5,3,6,4]
start = 0
end = 0
profit = 0

while end < len(prices):
    if prices[end] >= prices[start]:
        profit = max(profit, prices[end] - prices[start])
    else:
        start = end
    end += 1

print(profit)






