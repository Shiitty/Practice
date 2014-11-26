def calcHoldCost(requirements, initialInventory, prodPerMonth, holdingCostPerUnit):
    result = 0
    lastRemain = initialInventory
    for count in requirements:
        result += lastRemain * holdingCostPerUnit
        lastRemain = lastRemain + prodPerMonth - count
        if lastRemain < 0:
            lastRemain = 0
    return result
print calcHoldCost([10,10,10,10,10,10,10,10,10,10,10,10],0,0,15)
print calcHoldCost([10,10,10,10,10,10,10,10,10,10,10,10],10,10,15)
print calcHoldCost([40,50,60,40,50,60,40,50,60,40,50,60],0,50,10)
print calcHoldCost([110,70,40,20,10,100,15,40,120,70,10,80],70,50,15)