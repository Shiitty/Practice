0:337889first, last):
    result = last
    for i in range(last-1,first-1,-1):
        theMax = maxCommon(result, i)
        result = result*i/theMax
    return result
def maxCommon(a,b):
    while b!=0:
        c = a%b
        a=b
        b=c
    return a
print lcm(1,5)
print lcm(4,5)
print lcm(1,12)