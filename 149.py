def maxWait(arrival, service):
    readyToService = []
    result = []
    for (i,arr) in enumerate(arrival):
        if i == 0:
            readyToService.append(0)
            result.append(0)
            continue
        tmp1 = readyToService[i-1] + service[i-1]
        tmp = arrival[i-1] + service[i-1]
        if tmp >= tmp1:
            readyToService.append(tmp)
        else:
            readyToService.append(tmp1)
        tmp2 = readyToService[i] - arrival[i]
        if tmp2 < 0:
            tmp2 = 0
        result.append(tmp2) 
    return max(result)

print maxWait([3,3,9],[2,15,14])
print maxWait([182],[11])
print maxWait([2,10,11],[3,4,3])
print maxWait([2,10,12],[15,1,15])