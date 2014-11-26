def convertToMetric(strStandardTime):
    (hourStr,minuteStr,secondStr) = strStandardTime.split(':')
    hour = int(hourStr)
    minute = int(minuteStr)
    second = int(secondStr)
    seconds = hour*3600 + minute*60 + second
    metSeconds = seconds*100000/86400
    metHour =  metSeconds/10000
    metMinute = (metSeconds-metHour*10000)/100
    metSecond = metSeconds%100
    metMstr = ''
    metSstr = ''
    if metMinute<10:
        metMstr = '0'
    if metSecond<10:
        metSstr = '0'
    result = str(metHour)+':'+metMstr+str(metMinute)+':'+metSstr+str(metSecond)
    return result
    
print convertToMetric("01:45:17")
print convertToMetric("12:00:00")