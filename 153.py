import math
def monthlyOrder(sales, daysAvailable):
    total = 0
    aver = 0
    for (i, day) in enumerate(daysAvailable):
        if sales[i] > 0:
            aver += 1
        if day > 0:
            total += float(sales[i]) / float(day) * 30.0
    if aver > 0:
        return int(math.floor(total / aver))
    return 0

print monthlyOrder([5],[15])
print monthlyOrder([75,120,0,93],[24,30,0,30])
print monthlyOrder([8773],[16])
print monthlyOrder([1115,7264,3206,6868,7301],[1,3,9,4,18])
#print monthlyOrder([],[])