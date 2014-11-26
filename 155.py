import time
def possibleFathers(child, mother, men):
	result = []
	for (i, man) in enumerate(men):
		fsame = 0
		msame = 0
		psame = 0
		for (j,char) in enumerate(child):
			if char == man[j]:
				fsame += 1
			if char == mother[j]:
				msame += 1
			if man[j] == mother[j]:
				psame += 1
		if fsame<len(child)/2:
			continue;
		if fsame+msame-psame < len(child):
			continue
		result.append(i)
	print result
	return result

possibleFathers("ABCD","AXCY",["SBTD","QRCD"])
possibleFathers("ABCD","ABCX",["ABCY","ASTD","QBCD"])
possibleFathers("ABABAB","ABABAB",["ABABAB", "ABABCC", "ABCCDD", "CCDDEE"])
possibleFathers("YZGLSYQT","YUQRWYQT",["YZQLDPWT", "BZELSWQM", "OZGPSFKT", "GZTKFYQT", "WQJLSMQT"])
possibleFathers("WXETPYCHUWSQEMKKYNVP","AXQTUQVAUOSQEEKCYNVP",["WNELPYCHXWXPCMNKDDXD",  "WFEEPYCHFWDNPMKKALIW",  "WSEFPYCHEWEFGMPKIQCK",  "WAEXPYCHAWEQXMSKYARN",  "WKEXPYCHYWLLFMGKKFBB" ])
time.sleep(10)