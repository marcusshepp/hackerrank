import math

def encrypt(s):
	s = ''.join(s.split())
	rows = math.floor(math.sqrt(len(list(s))))
	columns = math.ceil(math.sqrt(len(list(s))))
	_list = []
	for i in range(len(list(s))):
		c = 0
		while c < columns:
			x = list(s)[int(rows):]
			_list.append(x)
			for j in x:
				s = list(s).remove(j)
			c+=1
	return _list

print encrypt("haveaniceday")