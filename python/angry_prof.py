def class_cancelled(numofstudneeded, arrivaltimes):
	ontime = 0
	for item in range(len(arrivaltimes)):
		if item <= 0:
			ontime += 1
	if ontime < numofstudneeded:
		return "YES"
	else:
		return "NO"

	

for item in range(int(raw_input())):
	s = raw_input()
	x = str(s).split()
	numofstudents = x[0]
	students_needed = x[1]
	x2 = raw_input()
	arrivals = str(x2).split()
	print class_cancelled(students_needed, arrivals)