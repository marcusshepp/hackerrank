foo = raw_input()
x = 0
for i in map(int, raw_input().split(" ")):
    if i < 0:
        x += 1
print x