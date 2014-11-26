def maxProfit(perDayCost, revenues):
    maxPro = 0
    curPro = 0
    for pro in revenues:
        tmpPro = pro - perDayCost
        curPro = curPro + tmpPro
        if curPro < 0:
            curPro = 0
        if maxPro < curPro:
            maxPro = curPro
    return maxPro

print maxProfit(20,[18,35,6,80,15,21])
print maxProfit(40,[30,20,10,38])
print maxProfit(10,[30,20,10,38])