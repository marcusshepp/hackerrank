"""
Problem Statement:

We will call a cell of the map a cavity if and only if this cell is not on the border of the 
map and each cell adjacent to it has strictly smaller depth. Two cells are adjacent if they have a common side (edge).

You need to find all the cavities on the map and depict them with the uppercase character X.

Input Format:

The first line contains an integer, n, denoting the size of the map. Each of the following n lines contains n 
positive digits without spaces. Each digit (1-9) denotes the depth of the appropriate area.

Output Format:

Output n lines, denoting the resulting map. Each cavity should be replaced with character X.

"""

def cavity_map(l):
	for i in range(1, len(l)-2):
		for j in range(1, len(l[i])-2):
			if l[i][j] == l[i+1][j]:
				 l[i][j] = "X"
				 l[i+1][j] = "X"
			elif l[i][j] == l[i+1][j+1]:
				 l[i][j] = "X"
				 l[i+1][j+1] = "X"				
	return l

x = int(raw_input())
l = [[]]*x
for i in range(x):
	l[i] = [int(x) for x in str(raw_input())]
l = cavity_map(l)
for i in range(len(l)):
	try:
		print int(''.join(map(str, l[i])))
	except ValueError:
		print ''.join(map(str, l[i]))

""" Your Cavity Map submission got 5.71 points. """