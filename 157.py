def howMuch(arrival, departure, wage):
	result = 0.0
	wageSecond = wage/3600.00
	for (i, atime) in enumerate(arrival):
		overtimeFlag = 0
		dtime = departure[i]
		aparts = atime.split(':')
		ahh = int(aparts[0])
		amm = int(aparts[1])
		ass = int(aparts[2])
		dparts = dtime.split(':')
		dhh = int(dparts[0])
		dmm = int(dparts[1])
		dss = int(dparts[2])
		if :
			