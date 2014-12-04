def getCycle(initial, current):
    result = 1
    init = list(initial)
    curr = list(current)
    while init != curr:
        result += 1
        if result > 4:
            break
        (init[2], init[3], init[1], init[0]) = (init[0], init[1], init[2], init[3])
    if result > 4:
        return -1
    return result
print getCycle('ABCD', 'ABCD')
print getCycle('ABCD', 'DCAB')
print getCycle('ABCD', 'CDBA')
print getCycle('ABCD', 'ABDC')
print getCycle('ZAXN', 'XNAZ')