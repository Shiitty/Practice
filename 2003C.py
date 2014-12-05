0:2577cdum(low, high, power):
    result = 0
    for p in range(1, power+1):
        for b in range(low, high+1):
            result += pow(b,p)
    return result
print getSum(1,3,2)
print getSum(-12,12,9)
print getSum(-100,100,2)