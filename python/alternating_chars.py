def find_minimum_deletions(s):
	""" 
	Given a string. 
	This function returns the minimum number of deletions it would take to
	make the string alternate between two chars.
	ex. 'ererereee' -> 2
	"""

	deletions = 0
	for i in range(len(list(s))-1):
		if s[i] == s[i+1]:
			deletions+=1
	return deletions

# for i in range(int(raw_input())):
# 	print find_minimum_deletions(raw_input())


print find_minimum_deletions("AAAA")
print find_minimum_deletions("BBBBB")
print find_minimum_deletions("abababab")
print find_minimum_deletions("BABABA")
print find_minimum_deletions("AAABBB")