import math
def getDivision(points):
    total = sum(points)
    result = []
    for point in points:
        tmp = point*100/total
        result.append(tmp)
    rest = 100 - sum(result)
    restMembers = []
    while rest>0:
        num = max(result)
        ind = result.index(num)
        restMembers.append((ind,num))
        result[ind] = 0
        rest -= 1
    #tmpMax = max(result)
    for (ind, num) in restMembers:
        #if num == tmpMax:
            #result[ind] = num
        #else:
            result[ind] = num + 1
    #(tmpInd,tmpNum) = restMembers[0]
    #result[tmpInd] += 100 - sum(result)
    return result
        

print getDivision([1,2,3,4,5])
print getDivision([5,5,5,5,5,5])
print getDivision([485, 324, 263, 143, 470, 292, 304, 188, 100, 254, 296, 255, 360, 231, 311, 275,  93, 463, 115, 366, 197, 470])