def maxProfit(prices):
    profit = 0
    buy, sell = 0, 1

    while sell < len(prices):
        if prices[sell] > prices[buy]:
            amount = prices[sell] - prices[buy]
            profit = max(profit, amount)
        else:
            buy += 1
        sell += 1
    
    return profit

print(maxProfit([7,1,5,3,6,4]))