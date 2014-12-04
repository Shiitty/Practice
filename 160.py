def avgMinutes(times):
    result = 0
    for (i, time) in enumerate(times):
        parts = time.split(', ')
        theTime = parts[0].split(' ')
        hm = theTime[0].split(':')
        ampm = theTime[1]
        theDate = parts[1].split(' ')
        h = int(hm[0])
        m = int(hm[1])
        day = int(theDate[1])
        totalTime = 0
        if ampm == 'AM':
            if h == 12:
                totalTime += (h+4)*60
                day -= 1
            else:
                totalTime += (h-8)*60
        else:
            if h==12:
                totalTime += (h-8)*60
            else:
                totalTime += (h+4)*60
        totalTime += m
        totalTime += (day-1) * 24 * 60
        result += totalTime
        #print totalTime
    print result
    theResult = result/len(times)
    check = result%len(times)
    if check*2>len(times):
        theResult += 1
    return theResult
print avgMinutes(["12:00 PM, DAY 1","12:01 PM, DAY 1"])
print avgMinutes(["12:00 AM, DAY 2"])
print avgMinutes(["02:00 PM, DAY 19","02:00 PM, DAY 20", "01:58 PM, DAY 20"])
        