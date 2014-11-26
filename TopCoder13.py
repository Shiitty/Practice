def isValid(word):
    word = word.lower()
    if len(word)==1:
        return 1
    #isValid = true
    vowCount = 0
    conCount = 0
    i = 0
    while i<len(word):
        #print word[i]
        if i>=len(word):
            return false
        while word[i] == 'a' or word[i] == 'e' or word[i] == 'o' or word[i]=='i' or word[i] == 'u':
            vowCount += 1
            i += 1
            if i>=len(word):
                return 0
        if i>=len(word):
            return 0
        while (word[i] != 'a' and word[i] != 'e' and word[i] != 'o' and word[i]!='i' and word[i] != 'u') and vowCount != 0:
            conCount += 1
            i += 1
            if i>=len(word):
                break
        #print vowCount, conCount
        if vowCount!=conCount:
            return 0
        elif vowCount + conCount == 0:
            i += 1
            vowCount = 0
            conCount = 0
        else:
            vowCount = 0
            conCount = 0
    return 1
print isValid("hi")
print isValid("Hih")
print isValid("Baaaiedddffaigg")
print isValid("H")