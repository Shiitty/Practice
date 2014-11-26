def biggestPower(n,p):
    result = 0
    couldDivide = True
    total = 1
    if n==0:
        return 0
    for i in range(1,n+1):
        total*=i
    while(total%(pow(p,result))==0):
        result += 1
    return result-1

print biggestPower(1,2)
print biggestPower(3,6)
print biggestPower(10,7)
print biggestPower(9,3)