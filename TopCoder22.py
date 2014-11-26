def getZbox(param0, param1):
    result = 0
    j = 0
    for i in range (param1,len(param0)):
        if param0[j] ==  param0[i]:
            result += 1
        else:
            break
        j += 1;
    return result

print getZbox("aabcaabca",0)
print getZbox("aabcaabca",1)
print getZbox("aabcaabca",2)
print getZbox("aabcaabca",3)
print getZbox("aabcaabca",4)
print getZbox("aabcaabca",5)
print getZbox("aabcaabca",6)
print getZbox("aabcaabca",7)
print getZbox("aabcaabca",8)