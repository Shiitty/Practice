06:324dfath
def numProcessors(k, overhead):
    minTime = k
    result = 2
    currentTime = overhead + k/2
    while currentTime<minTime:
        result += 1
        minTime = currentTime
        overheads = overhead*result*(result-1)/2
        currentTime = overheads + int(math.ceil(float(k)/float(result)))
    return result-1
print numProcessors(12,1)
print numProcessors(50,3)
print numProcessors(9,10)
print numProcessors(3333,2)
print numProcessors(1000000, 4)