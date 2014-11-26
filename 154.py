def matches(keyPresses, codes):
    result = []
    for (i,code) in enumerate(codes):
        keyInd = 0
        codeInd = 0
        matched = True
        while keyInd < len(keyPresses):
            tmpChar = keyPresses[keyInd]
            tmpKeyCount = 0
            tmpCodeCount = 0
            while keyInd < len(keyPresses) and keyPresses[keyInd] == tmpChar:
                keyInd += 1
                tmpKeyCount += 1
            while codeInd < len(code) and code[codeInd] == tmpChar:
                codeInd += 1
                tmpCodeCount += 1
            print(str(tmpKeyCount)+","+str(tmpCodeCount))
            if tmpCodeCount > tmpKeyCount:
                matched = False
        if matched:
            result.append(i)
    return result

print matches("UUDDLRRLLRBASS", ["UUDDLRLRBA",  "UUDUDLRLRABABSS",  "DDUURLRLAB",  "UUDDLRLRBASS",  "UDLRRLLRBASS"])
            