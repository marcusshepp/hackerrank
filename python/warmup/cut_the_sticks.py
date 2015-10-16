def stickit(l):
	f = lambda x: x-min(l)
	l = [f(x) for x in l]
	return filter(lambda a: a > 0, l)

raw_input()
l = raw_input()
_input = [int(x) for x in l.split()]
print len(_input)
while stickit(_input) != []:
	print len(stickit(_input))
	_input = stickit(_input)