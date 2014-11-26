def getMod(al):
    ai = []
    bi = []
    result = -1
    bound = 1
    notfit = 1
    for pair in al:
        (a,b) = pair.split(',')
        ai.append(int(a))
        bi.append(int(b))
    for j in range(0,len(ai)):
        bound *= ai[j]
    while notfit:
        result += 1
        for i in range(0,len(ai)):
            notfit = 0
            if result%ai[i] != bi[i]:
                notfit = 1
                break;
        if result>bound:
            return -1

    return result
print getMod({"2,1","3,1","5,1"})
print getMod({"7,2", "9,3"})
print getMod({"4,3", "8,4"})