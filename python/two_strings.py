def common_substring(s1, s2):
	"""
	You are given two strings, A and B. 
	Find if there is a substring that appears in both A and B.
	"""

	x, y = list(s1), list(s2)
	flag = ""
	for a in x:
		if a in y:
			flag = "yes"
		else:
			flag = "no"
	return flag

for _ in range(int(raw_input())):
	x = str(raw_input())
	y = str(raw_input())
	print common_substring(x, y)