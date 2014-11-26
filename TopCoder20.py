def sortByLength(param):
    helper = []
    result = param
    for string in param:
        helper.append(len(string))
    for i in range(0,len(helper)):
        for j in range(0,len(helper)):
            if helper[i]>helper[j]:
                tmph = helper[i]
                tmps = result[i]
                helper[i] = helper[j]
                helper[j] = tmph
                result[i] = result[j]
                result[j] = tmps
    return result
print sortByLength(["Top", "Coder", "comp", "Wedn", "at", "midnight"])
print sortByLength(["one", "three", "five"])
print sortByLength(["I","love","Cpp"])