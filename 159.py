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
print freeParks('SSD-B---BD-DDSB-----S-S--------S-B----BSB-S--B-S-D')