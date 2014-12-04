05:48f07ify(textIn):
    maxLen = 0
    result = []
    for name in textIn:
        if maxLen < len(name):
            maxLen = len(name)
    for (i,names) in enumerate(textIn):
        tmp = ""
        for i in range(0, maxLen-len(names)):
            tmp += " "
        result.append(tmp + names)
    return result
print justify(["BOB","TOMMY","JIM"])
print justify(["JOHN","JAKE","ALAN","BLUE"])
print justify(["LONGEST","A","LONGER","SHORT"])