container = list()
ns = list()
while True:
    i = raw_input()
    if i == "0":
        break
    else:
        ns.append(i)
print ns
for i in ns:
    ii = int(i)
    t = list()
    for a in i:
        t.append(a)
    t = map(int, t)
    total = sum(t)
    x = 10
    while True:
        nn = ii * x
        n = str(nn)
        n = [a for a in n]
        n = map(int, n)
        n = sum(n)
        if n == total:
            print nn
            break
        x += 1