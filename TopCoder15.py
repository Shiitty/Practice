def getMagicNumber(strName):
    strName = strName.lower()
    numBer = 0
    result1 = 100
    for char1 in strName:
        if char1 == ' ':
            continue
        numBer += (ord(char1)-ord('a') + 1)
    while result1 >= 10:
        result1 = 0
        while numBer > 0:
            result1 += numBer%10
            numBer = numBer/10
        numBer = result1
    return result1

print getMagicNumber("Mandy Dean Thompson")
print getMagicNumber("Nate Tina Tanner")
print getMagicNumber("Paul Tim Brown")
print getMagicNumber("Ralph Amber Black")
print getMagicNumber("Bill Susan Burton")