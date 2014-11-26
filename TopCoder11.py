def lookup(k):
    count = 0
    tmp = -1
    while(count<k):
        tmp = tmp + 1
        if tmp%2 == 0 or tmp%3==0 or tmp%5==0:
            count = count + 1
    return tmp

print lookup(20)