def getResult(a,op,b):
    result = 0
    if op=='+':
        result = a+b
    elif op=='*':
        result = a*b
    else:
        return [-1,-1]
    return [result%256, result/256]
print getResult(200,'+',3)
print getResult(200,'+',0)
print getResult(200,'+',56)
print getResult(255,'+',0)
print getResult(255,'+',255)
print getResult(200,'*',3)
print getResult(200,'*',0)
print getResult(200,'*',56)
print getResult(255,'*',1)
print getResult(255,'*',255)