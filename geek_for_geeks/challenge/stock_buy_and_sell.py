# 7 - Stock Buy and Sell (With No Limit)
# Best Approach
def maximumProfit(prices):
    n = len(prices)
    res = 0
    for i in range(0, n - 1, 1):
        if prices[i] < prices[i + 1]:
            res += prices[i + 1] - prices[i]
    return res


# T.C: O(n)
# S.C: O(1)

# def maximumProfit(prices):
#     n = len(prices)
#     res = 0
#     lmin = prices[0]
#     lmax = prices[0]
#     i = 0
#     while i < n - 1:
#         while i < n - 1 and prices[i] >= prices[i]:
#             i += 1
#         lmin = prices[i]
#         while i < n - 1 and prices[i] <= prices[i]:
#             i += 1
#         lmax = prices[i]
#         res += lmax - lmin
#     return res

# T.C: O(n)
# S.C: O(1)
