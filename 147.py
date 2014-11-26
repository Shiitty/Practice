def order(numMales, numFemales, K):
    totalCount = numMales + numFemales
    result = []
    for i in range(0,totalCount):
        result += 'M'
    ind = 0
    count = 0
    while numFemales > 0:
        if count == K-1:
            #ind += 1
            result[ind%totalCount] = 'F'
            count = 0
            numFemales -= 1
        if result[ind%totalCount]=='F':
            ind += 1
            continue
        else:
            count += 1
            ind += 1
    strResult = ""
    for char in result:
        strResult += char
    return strResult

print order(5,3,2)
print order(7,3,1)
print order(25,25,1000)
print order(5,5,3)
print order(1,0,245)        