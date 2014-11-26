def parseInt(param):
    result = 0
    nothing = True
    for char in param:
        if ord('0')<=ord(char)<=ord('9'):
            result = result*10 + ord(char)-ord('0')
            nothing = False
        if char == 'o' or char == 'O':
            result = result*10 + 0
            nothing = False
        if char == 'l':
            result = result*10 + 1
            nothing =  False
    if nothing:
        return -1
    return result

print parseInt("lo6")
print parseInt("234,657")
print parseInt("hi")
print parseInt(",,,,,5,,5,  4")
print parseInt("2200000000")
            