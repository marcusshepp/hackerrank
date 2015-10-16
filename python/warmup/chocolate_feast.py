"""
Problem Statement:

Little Bob loves chocolate, and he goes to a store with $N in his pocket. 
The price of each chocolate is $C. The store offers a discount: 
for every M wrappers he gives to the store, he gets one chocolate for free. 
How many chocolates does Bob get to eat?

Input Format: 
The first line contains the number of test cases, T. 
T lines follow, each of which contains three integers, N, C, and M.

Output Format: 
Print the total number of chocolates Bob eats.
"""

def chocolate(money, cost, wrappers):
	c = 0
	for i in range(1, money):
		if i % money == 0:
			c += 1
	if c % wrappers == 0
