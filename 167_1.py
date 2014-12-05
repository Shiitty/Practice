06:9+13fate(speed, init):
    tmpinit = init
    tmpinit.replace('L','-1')
    tmpinit.replace('R', '1')
    tmpinit.replace('.', '100')
    initList = []
    result = []
    for (i, char) in enumerate(initList):
        initList.append(int(char))
    tmpresult = init
    tmpresult.replace('L', 'X')
    tmpresult.replace('R', 'X')
    empty = str('.', len(init))
    result.append(tmpresult)
    while  tmpresult != empty:
        