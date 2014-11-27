def getBase(equation):
	parts1 = equation.split('+')
	firstNum = list(parts1[0])
	parts2 = parts1[1].split('=')
	secondNum = list(parts2[0])
	resultNum = list(parts2[1])
	result = []
	minBase = 2
	for i in xrange(0,len(resultNum)):
		if i<len(firstNum):
			if firstNum[i] < 'A':
				firstNum[i] = int(firstNum[i])
			else:
				firstNum[i] = ord(firstNum[i])-ord('A')+10
			if minBase<firstNum[i]:
				minBase=firstNum[i]
		if i<len(secondNum):
			if secondNum[i] < 'A':
				secondNum[i] = int(secondNum[i])
			else:
				secondNum[i] =  ord(secondNum[i])-ord('A')+10
			if minBase<secondNum[i]:
				minBase=secondNum[i]
		if i<len(resultNum):
			if resultNum[i]<'A':
				resultNum[i] = int(resultNum[i])
			else:
				resultNum[i] = ord(resultNum[i])-ord('A')+10
			if minBase<resultNum[i]:
				minBase=resultNum[i]
	for base in xrange(minBase,21):
		ind = 1
		num1 = firstNum[len(firstNum)-ind]
		num2 = secondNum[len(secondNum)-ind]
		res = resultNum[len(resultNum)-ind]
		addup = 0
		while (num1+num2+addup)%base==res:
			ind += 1
			if ind>len(resultNum):
				break
			if num1+num2+addup>=base:
				addup = 1
			else:
				addup = 0
			tmp1 = len(firstNum)-ind
			if tmp1 < 0:
				num1=0
			else:
				num1 = firstNum[tmp1]
			tmp2 = len(secondNum)-ind
			if tmp2 < 0:
				num2=0
			else:
				num2 = secondNum[tmp2]
			tmpres = len(resultNum)-ind
			if tmpres<0:
				break
			else:
				res = resultNum[tmpres]
		if ind > len(resultNum):
			result.append(base)
	print result
getBase('1+1=2')
getBase('1+1=10')
getBase('ABCD+211=B000')
getBase('ABCD+322=B000')
getBase('1+0=1')
getBase('GHIJ+1111=HJ00')
getBase('1234+8765=9999')