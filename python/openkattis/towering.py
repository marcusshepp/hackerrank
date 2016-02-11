import itertools

inp = raw_input().split(" ")
total_one = int(inp[-1])
total_two = int(inp[-2])
boxes = inp[0:6]
container = list()
for i in itertools.permutations(boxes, 3):
    x = sorted(map(int, i))[::-1]
    if sum(map(int, i)) == total_one or sum(map(int, i)) == total_two:
        if x not in container:
            container.append(x)
p = list()
for i in container:
    for a in i:
        p.append(a)
print " ".join([str(a) for a in p])