0:2310b9est(sleepTime, k):
    if k==1:
        return 60*24.0
    result = (24.0-sleepTime)/float(k-1)*60.0
    return result
print closest(8,2)
print closest(9,3)
print closest(23,1)
print closest(9,8)