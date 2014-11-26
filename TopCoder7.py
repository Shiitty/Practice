def parse(toParse):
    parser = toParse[0]
    parseList = toParse.split(parser)
    resultList = []
    for tmp in parseList:
        if len(tmp)>0:
            resultList[0:0] = [tmp]
    return resultList

print parse(".period.is.the..delimiter")
print parse("AAthisAAAisAaAAtestAAA")