#!/usr/bin/python
# -*- coding: ascii -*-
"""	Your task is to help him find the minimum number of characters of the first string he needs to 
	change to enable him to make it an anagram of the second string.

	Note: A word x is an anagram of another word y if we can produce y by rearranging the letters of x.

	Input Format The first line will contain an integer, T, representing the number of test cases. 
	Each test case will contain a string having length len(S1)+len(S2), 
	which will be concatenation of both the strings described above in the problem.
	The given string will contain only characters from a to z.

	Output Format An integer corresponding to each test case is printed in a different line, 
"""

def min_del(s):
	c_ = 0
	_u = len(s)
	q_ = list(s)
	if _u % 2 == 0:
		l_side = q_[_u/2:]
		r_side = q_[:_u/2]
		pok = {}
		for i in l_side:
			if i in pok:
				pok[i] += 1
			else:
				pok[i] = 1
		for j in r_side:
			if j in pok:
				if pok[j] > 0:
					pok[j] -= 1
			else:
				c_ += 1
		for x in pok:
			if pok[x] > 0:
				c_ += 1
	else:
		c_ = -1
	return c_

# for i in range(int(raw_input())):
# 	print min_del(str(raw_input()))

print "10 -- ", min_del("hhpddlnnsjfoyxpciioigvjqzfbpllssuj")
print "13 -- ", min_del("xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj")
print "5 -- ", min_del("dnqaurlplofnrtmh")
print "26 -- ", min_del("aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb")
print "15 -- ", min_del("lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad")
print "-1 -- ", min_del("drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe")
print "3 -- ", min_del("ubulzt")
print "13 -- ", min_del("vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy")
print "13 -- ", min_del("xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa")
print "-1 -- ", min_del("gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv")

"""
10
13
5
26
15
-1
3
13
13
-1
"""