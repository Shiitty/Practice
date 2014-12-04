import math
def numFolds(paper, box):
    result = 0
    x1 = float(paper[0])/float(box[0])
    y1 = float(paper[1])/float(box[1])
    x2 = float(paper[0])/float(box[1])
    y2 = float(paper[1])/float(box[0])
    if x1+y1 < x2+y2:
        x = math.floor(math.log(x1, 2))
        y = math.floor(math.log(y1, 2))
        result =  x + y
    else:
        x = math.floor(math.log(x2, 2))
        y = math.floor(math.log(y2, 2))
        result = result+x+y
    if result > 8:
        return -1
    if result < 0:
        return 0
    return result
    
print numFolds([8, 11], [6, 10])
print numFolds([11, 17],[6, 4])
print numFolds([11, 17],[5, 4])
print numFolds([1000,1000],[62,63])
print numFolds([100,30],[60,110])
print numFolds([1895, 6416],[401, 1000])