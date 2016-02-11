n = int(raw_input().strip())

def buildstr(spaces, hashes):
    i = "".join([" " for a in range(spaces)])
    i += "".join(["#" for a in range(hashes)])
    return i
for i in range(n):
    print buildstr(n - 1, i + 1)
    n = n - 1