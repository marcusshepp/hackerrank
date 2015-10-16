def min_ops(s):
	s = [ord(_) for _ in list(s)]
	c = 0
	if s != s[::-1]:
		z = zip(s, s[::-1])
		for i,j in z:
			while i != j:
				if i > j:
					c += 1
					i -= 1
				else:
					c += 1
					j -= 1
	return c/2

for i in range(int(raw_input())):
	print min_ops(str(raw_input()))