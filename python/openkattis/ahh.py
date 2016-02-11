jon = raw_input()
doc = raw_input()

def noh(s):
    return [a for a in s if a != "h"]
jon = noh(jon)
doc = noh(doc)
if len(jon) >= len(doc):
    print "go"
else:
    print "no"