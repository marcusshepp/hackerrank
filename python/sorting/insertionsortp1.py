def insertionsort(l):
	value = l[len(l)-1]
	time = ""
	for i in reversed(l):
		if i > value:
			# print "l[l.index(i)]: ", l[l.index(i)]
			l[l.index(i)+1] = i
		if i <= value:
			print "l.index(i)+1: ", l.index(i)+1
			l[l.index(i)-1] = value
		time+=str(l)+"\n"
	return time

print insertionsort([2, 4, 6, 8, 3])