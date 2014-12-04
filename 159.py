<<<<<<< HEAD
<<<<<<< HEAD
def howLong(panSize, humbargers):
    timeNum = humbargers*2/panSize
    if humbargers%panSize!=0:
        timeNum+=1
    return timeNum*5

print howLong(3,4)
print howLong(3,2)
print howLong(100,0)
print howLong(303,919)
    
=======
=======
>>>>>>> FETCH_HEAD
def freeParks(street):
	strList = list(street)
	result = 0
	for (i, char) in enumerate(strList):
		if char == 'B':
			if i-1 > 0:
				if strList[i-1]=='-':
					strList[i-1]='*'
			if i-2 > 0:
				if strList[i-2]=='-':
					strList[i-2]='*'
		if char == 'S':
			if i-1>0:
				if strList[i-1]=='-':
					strList[i-1]='*'
			if i+1<len(strList)-1:
				if strList[i+1]=='-':
					strList[i+1]='*'
	for char in strList:
		if char == '-':
			result += 1
	return result
print freeParks('---B--S-D--S--')
print freeParks('DDBDDBDDBDD')
print freeParks('--S--S--S--S--')
<<<<<<< HEAD
print freeParks('SSD-B---BD-DDSB-----S-S--------S-B----BSB-S--B-S-D')
>>>>>>> FETCH_HEAD
=======
print freeParks('SSD-B---BD-DDSB-----S-S--------S-B----BSB-S--B-S-D')
>>>>>>> FETCH_HEAD
