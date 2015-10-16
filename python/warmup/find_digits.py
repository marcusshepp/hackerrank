"""
You are given an integer N. Find the digits in this number that exactly divide N 
(division that leaves 0 as remainder) and display their count. 
For N=24, there are 2 digits (2 & 4). Both of these digits exactly divide 24. 
So our answer is 2.

Note

If the same number is repeated twice at different positions, 
it should be counted twice, e.g., For N=122, 2 divides 122 exactly and occurs at ones' 
and tens' position. So for this case, our answer is 3.
Division by 0 is undefined.
"""

def f(l, n):
	x = [i for i in l if i != 0]
	x = [i for i in x if n%i == 0]
	return x

def find_digits(hmm):
	_s = [int(x) for x in str(hmm)]
	_s = f(_s, hmm)
	return len(_s) 

for i in range(int(raw_input())):
	print find_digits(int(raw_input()))