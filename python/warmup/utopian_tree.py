"""
The Utopian Tree goes through 2 cycles of growth every year. 
The first growth cycle occurs during the spring, when it doubles in height. 
The second growth cycle occurs during the summer, when its height increases by 1 meter.

Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter. 
Can you find the height of the tree after N growth cycles?
"""

def tree_height(t):
	""" Returns the height of a Utopian tree. Takes the input of the number of cycles. """

	height = 1
	if t == 0:
		return 1
	if t == 1:
		return 2
	else:
		for i in range(t):
			if i%2 == 0:
				height *= 2
			else:
				height += 1
			print "height: ", height

		return height

for _ in range(int(raw_input())):
	print tree_height(int(raw_input()))