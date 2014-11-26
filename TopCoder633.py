def minimalTime(x, jumpLengths):
    upper = abs(x)
    lower = abs(x)
    j = 0
    length = len(jumpLengths)
    while not(lower<=jumpLengths[j%length]<=upper):
        tmp1 = abs(lower - jumpLengths[j%length])
        tmp2 = abs(lower + jumpLengths[j%length])
        tmp3 = abs(upper - jumpLengths[j%length])
        tmp4 = abs(upper + jumpLengths[j%length])
        lower = min(tmp1, tmp2, tmp3, tmp4)
        upper = max(tmp1, tmp2, tmp3, tmp4)
        j += 1
    return j+1
print minimalTime(5,[5])
print minimalTime(15,[1,2,3,4,5,6,7,8,9,10])
print minimalTime(1,[10])
print minimalTime(-10000,[1])
print minimalTime(-10,[2,3,4,500,6,7,8])
         