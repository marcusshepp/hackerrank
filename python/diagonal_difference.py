from copy import deepcopy

thematrix = []
for i in xrange(int(raw_input())):
    thematrix.append([int(x) for x in raw_input().split()])

def dia_diff(matrix):
    size = len(matrix[0])
    copy_size = deepcopy(size)
    forward_slash = []
    backward_slash = []
    y1 = 0
    y2 = size - 1
    while copy_size:
        copy_size -= 1
        forward_slash.append(matrix[copy_size][y1])
        y1 += 1
        backward_slash.append(matrix[copy_size][y2])
        y2 -= 1
    thesum = sum(backward_slash) - sum(forward_slash)
    return abs(thesum)

print dia_diff(thematrix)
