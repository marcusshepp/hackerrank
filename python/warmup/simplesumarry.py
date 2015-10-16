x = 0
length = int(raw_input())
y = raw_input()
y = map(int, y.split())
for i in xrange(length):
    re = int(y[i])
    x += re
print x