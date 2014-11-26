def overLap(hour):
    formAngle = hour * 30
    while formAngle >= 360:
        formAngle -= 360
    seconds = formAngle*120.0/11.0
    seconds = int(seconds)
    minute = seconds/60
    second = seconds%60
    minuteS = ''
    secondS = ''
    if minute<10:
        minuteS += '0'
    if second<10:
        secondS += '0'
    return str(hour)+':'+minuteS+str(minute)+':'+secondS+str(second)
    
print overLap(9)