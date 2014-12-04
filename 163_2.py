04:274fbhtime(branch, rest, leaf):
    result = 0
    for i in range(0, branch+1, rest):
        if i%leaf==0:
            result += 1
    return result
    
print lunchtime(11, 2, 4)
print lunchtime(12, 6, 4)
print lunchtime(20, 3,7)
print lunchtime(21, 7, 3)
print lunchtime(15, 16, 1)
print lunchtime(1000, 3, 7)
print lunchtime(1000, 7, 3)