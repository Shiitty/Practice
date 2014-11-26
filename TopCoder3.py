def compare(input1, input2):
    count = 0
    for char1 in input1:
        print count
        for i,char2 in enumerate(input2):
            if char1 == char2:
                count = count + 1
                input2 = input2[:i-1]+'\0'+input2[i+1:]
                break
    return count

print compare("foobar", "sing")
