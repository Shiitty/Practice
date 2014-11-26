def combine(s1,s2):
    longer1 = len(s1) > len(s2)
    length = max(len(s1), len(s2))
    shortlength = min(len(s1), len(s2))
    count=0
    result = ""
    while(count<shortlength):
        result = result + s1[count] + s2[count]
        count = count + 1
    if longer1:
        result = result + s1[count:length]
    else:
        result = result + s2[count:length]
    return result
print combine("aa","bb")
print combine("Tpo","oCder")
    