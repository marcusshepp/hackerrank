"""
Given two strings (they can be of same or different length) help her 
in finding out the minimum number of character deletions required to make
two strings anagrams. Any characters can be deleted from any of the strings.

Two strings are anagrams of each other if they have same character set.
For example strings "bacdc" and "dcbac" are anagrams, while strings "bacdc" and "dcbad" are not.
"""

def count(stringone, stringtwo):
    """ returns number on min del. """

    s1, s2 = sorted(list(stringone)), sorted(list(stringtwo))
    x1, x2 = sorted(list(stringone)), sorted(list(stringtwo))
    x = max(len(s1), len(s2))
    for i in range(x):
    	if i > len(s1)-1 or i > len(s2)-1:
    		break
        else:
        if s1[i] in s2 or s2[i] in s1:
            x1.remove(s1[i])
            x2.remove(s2[i])
    return len(x1+x2)



# one = str(raw_input())
# two = str(raw_input())
# print count(one, two)
print count("cde", "abc")