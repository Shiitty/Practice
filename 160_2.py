0ef getValue(key, code):
    result = ""
    for char in code:
        i = key.find(char)
        if i>=0:
            i+=1
        if i==10:
            i=0
        string = ""
        if i>=0:
            string = str(i)
        result += string
    return int(result)
print getValue("TRADINGFEW", "LGXWEV")
print getValue("ABCDEFGHIJ", "XJ")
print getValue("CRYSTALBUM", "MMA")
        