02:18c07s(pence):
    result = []
    pound = pence/240
    shilling = (pence%240)/12
    penis = pence%12
    return [pound, shilling, penis]

print coins(533)
print coins(0)
print coins(6)
print coins(4091)
print coins(10000)