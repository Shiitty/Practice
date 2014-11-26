def isShaky(para):
    if para <= 10:
        return 1;
    nums = []
    while para > 0:
        nums.append(para%10)
        para/=10
        #print para
    if len(nums)==2:
        if nums[0]==nums[1]:
            return 0
        else:
            return 1
    for i in range(1,len(nums)-1):
        tmpa = nums[i-1] - nums[i]
        tmpb = nums[i] - nums[i+1];
        if tmpa * tmpb >= 0:
            return 0
    return 1
print isShaky(5252)
print isShaky(2525)
print isShaky(25)
print isShaky(52)
print isShaky(8)
print isShaky(33)
print isShaky(521)
print isShaky(23234)