def bigger_is_greater(s):
	"""
	Given a word w, rearrange the letters of w to 
	construct another word s in such a way that s is lexicographically greater than w. 
	In case of multiple possible answers, find the lexicographically smallest one.
	"""
	array = []
	for _ in s:
		array.append(ord(_))
	sort = sorted(array)
	if sort == array:
		return "no answer"
	else:
		for n in range(len(sort)):
			sort[n] = chr(sort[n])
		return "".join(sort)
		
for _ in range(int(raw_input())):
    print bigger_is_greater(raw_input())