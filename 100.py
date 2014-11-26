def decode(message):
    result1 = ""
    result2 = ""
    false1 = False
    false2 = False
    if len(message)==1:
        return("None","None")
    for (i,char) in enumerate(message):
        if i == (len(message) - 1):
            if false1 == False:
                if int(result1[i])+int(result1[i-1]) != int(char):
                    false1 = True
            if false2 == False:
                if int(result2[i]) + int(result2[i-1]) != int(char) and false2 == False:
                    false2 = True
            break
        if i == 0:
            tmp1 = '0'
            tmp2 = '1'
            result1 = result1 + tmp1
            result2 = result2 + tmp2
            tmp1 = str(int(char) - 0)
            tmp2 = str(int(char) - 1)
            if int(tmp1)<=1 and false1 == False:
                result1 = result1 + tmp1
            else:
                false1 = True
            if int(tmp2)<=1 and false2 == False:
                result2 = result2 + tmp2
            else:
                false2 = True
        else:
            if false1 == False:
                tmp1 =  str(int(char)-int(result1[i-1]) - int(result1[i]))
            if false2 == False:
                tmp2 = str(int(char)-int(result2[i-1])- int(result2[i]))
            if tmp1 == '0' or tmp1 == '1':
                result1 = result1+tmp1
            else:
                false1 = True
            if tmp2 == '0' or tmp2 == '1':
                result2 = result2 + tmp2
            else:
                false2 = True
    if false1:
        result1 = "None"
    if false2:
        result2 = "None"
    return (result1, result2)
    
(a,b) = decode("23210")
print a+', '+b