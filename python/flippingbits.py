"""
You will be given a list of 32 bits unsigned integers. 
You are required to output the list of the unsigned integers 
you get by flipping bits in its binary representation 
(i.e. unset bits must be set, and set bits must be unset).
"""

def bitrep(n):
	""" Returns the signed 32-bit binary representation of an integer. """
	arr = []
	reversed_arr = []
	j=0
	while j<32:
		x=n%2
		if x>0:
			arr.append(1)
		else:
			arr.append(0)
		n/=2
		j+=1
	for i in reversed(arr):
		reversed_arr.append(i)
	return reversed_arr

def flip(a):
	""" 
	return the opposite of a bitrep.
	110 becomes 001
	"""
	j=0
	while j<len(a):
		if a[j] == 0:
			a[j] = 1
		else:
			a[j] = 0
		j+=1
	return a

def convert_to_int(a):
	""" 
	converts an array of numbers that represent a binary representation of an integer,
	into the actual integer.
	"""
	l = len(a)
	power = l - 1
	equation = []
	for i in range(0, l):
		multi_c = a[i]
		num = a[i]*2**power
		equation.append(num)
		power-=1
	return sum(equation)

def flipping_bits():
	return convert_to_int(flip(bitrep(0)))

n = int(raw_input())
for i in range(0,n):
    a = n.split()
    res = flipping_bits(a)
    print res

print "----"
print "binary rep: ", ''.join(str(e) for e in bitrep(0))
print "----"
print "\n"
print "----"
print "flipped: ", ''.join(str(e) for e in flip(bitrep(0)))
print "----"
print "\n"
print "----"
print "converted to int: ", convert_to_int(flip(bitrep(0))) # <-- final answer
print "----"