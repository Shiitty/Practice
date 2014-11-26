def countRectangles(width, length):
    count = 0
    for i in range(1,width+1):
        for j in range(1,length+1):
            if i!=j:
                lengthCount = length - j + 1
                widthCount = width - i + 1
                #print lengthCount * widthCount    
                count += lengthCount * widthCount
    return count
    
print countRectangles(3,3)
print countRectangles(5,2)
print countRectangles(10,10)
print countRectangles(1,1)
print countRectangles(592,964)