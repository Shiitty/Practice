def minDrives(used, total):
	allData = sum(used);
	for (j, disk1) in enumerate(total):
		for (k, disk2) in enumerate(total):
			if k==j:
				continue
			if total[k]<total[j]:
				(total[k],total[j])=(total[j],total[k])
	print total
	for (i, disk) in enumerate(total):
		allData = allData - disk
		if allData<=0:
			return i+1
	return len(total)

print minDrives([331,242,384,366,428,114,145,89,381,170,329,190,482,246,2,38,220,290,402,385],[992,509,997,946,976,873,771,565,693,714,755,878,897,789,969,727,765,521,961,906])