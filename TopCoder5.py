def compress(toCompress):
    inLen = len(toCompress)
    result = ""
    count = 1
    tmpChar = ''
    i= 1
    while i < inLen:
        tmpChar = toCompress[i]
        while toCompress[i]==tmpChar:
            print i
            count = count + 1
            i = i+1
            if i>=inLen:
                break
        if count>1:
            result = result + "%s"%count
        count = 0
        result =  result + tmpChar
    return result
    
print compress("AAAABBBBCDDDDDD")