def buy_sell(prices):
    buy=prices[0]
    max_profit=0
    for i in range(len(prices)):
        if buy>prices[i]:
            buy=prices[i]
        elif prices[i]-buy>max_profit:
            max_profit=prices[i]-buy
    return max_profit




prices=list(map(int,input('enter the array element: ').strip().split())) # prices = [7,6,4,3,1]
print(buy_sell(prices)) # 0

# output: [7,1,5,3,6,4] # 5