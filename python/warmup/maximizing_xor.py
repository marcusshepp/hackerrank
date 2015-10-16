"""
	Given two integers, L and R, find the maximal value of A xor B, 
	where A and B satisfy the following condition:

	L ≤ A ≤ B ≤ R
"""

def maxXor(l , r):
    array = []
    while l <= r:
        for key in range(l, r):
            array.append(l^key)
        l = l + 1
        # r = r + 1
    return max(array)

res = maxXor(10, 15)
print res
