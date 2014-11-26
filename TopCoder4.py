def encoder(input1):
    inputLen = len(input1)
    input1 = input1 + "     "
    tmp = input1.replace(' ','~')
    if inputLen % 5:
        inputLen = (inputLen/5 + 1)*5
    result = ""
    for l in range(0,5):
        for r in range(0,inputLen/5):
            result = result + tmp[l+r*5]
    
    result =  result + '$'
    return result
    
    
print encoder("THIS CODED MESSAGE")
print encoder("TopCoder is cool")
        
        