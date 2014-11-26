def getDaysOld(birthdate, currdate):
    daysInMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    (birthMonthS,birthDayS,birthYearS) = birthdate.split('/')
    (currentMonthS,currentDayS,currentYearS) = currdate.split('/')
    birthMonth = int(birthMonthS)
    birthDay = int(birthDayS)
    birthYear = int(birthYearS)
    currMonth = int(currentMonthS)
    currDay = int(currentDayS)
    currYear = int(currentYearS)
    totalDay = (currYear - birthYear)*365
    month = range(min(currMonth,birthMonth)-1, max(currMonth,birthMonth)-1)
    totalMonth = 0
    if currMonth != birthMonth:
        for i in month:
            totalMonth = totalMonth + daysInMonths[i]
        totalDay = totalMonth * (currMonth - birthMonth)/abs(currMonth - birthMonth) + totalDay
    totalDay = totalDay + currDay - birthDay
    if currYear - birthYear > 1:
        totalYear = range(birthYear+1,currYear)
        for j in totalYear:
            if j%4==0:
                totalDay = totalDay + 1
    if birthYear%4==0 and birthMonth<=2:
            totalDay = totalDay + 1
    if currYear%4==0 and currMonth>2:
            totalDay = totalDay + 1
    print totalDay

getDaysOld("10/10/1999","10/10/2000")