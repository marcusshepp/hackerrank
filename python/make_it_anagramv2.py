def count(s1, s2):
	coffee = {}
	water = {}
	c = 0
	for i in list(s1):
		if i not in coffee:
			coffee[i] = 1
		else:
			coffee[i] += 1
	for i in list(s2):
		if i not in water:
			water[i] = 1
		else:
			water[i] += 1
	for i in coffee.iterkeys():
		if i > len(coffee) or i > len(water):
			break
		c += abs(coffee[i] - water[i])
	return c

print count("cde", "abc")