def stocks(prices):
    maxProfit = float('-inf')
    minPrice = float('inf')

    for price in prices: 
        minPrice = min(minPrice, price)
        maxProfit = max(price - minPrice, maxProfit)
    return maxProfit

print(stocks([7,1,5,3,6,4]))

"""
Time Complexity = O(N)
Space Complexity = O(1)
"""