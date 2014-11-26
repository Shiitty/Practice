def getProfit(prices):
    maxProfit = 0
    currentProfit = 0
    #elementCount = prices.length()
    #if elementCount==1:
    #    return 0
    tmp = prices[0]
    for price in prices:
        if price<=0 or tmp <=0:
            break
        currentProfit += price - tmp
        tmp = price
        if maxProfit < currentProfit:
            maxProfit = currentProfit
    return maxProfit

prices=[80,70,40,3,2,1]
print getProfit(prices)
        
        