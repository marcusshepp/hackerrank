num, str_one, str_two = int(raw_input()), raw_input(), raw_input()

def switch(s):
    x = str()
    for i in range(len(s)):
        if s[i] == "0": x+="1"
        else: x+="0"
    return x

x = str_one
for i in range(num):
    x = switch(x)

if x == str_two: print "Deletion succeeded"
else: print "Deletion failed"