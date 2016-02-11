time = raw_input().strip()
def dothething(time):
    time = time.split(":")
    h = time[0]
    m = time[1]
    s = time[2][0:2]
    ap = time[2][2:4]
    if ap == "AM":
        if int(h) < 10:
            return "0" + h + ":" + m + ":" + s
        else:
            return h + ":" + m + ":" + s
    elif ap == "PM":
        h = int(h) + 12
        return str(h) + ":" + m + ":" + s
if time == "12:00:00AM":
    print "00:00:00"
elif time == "12:00:00PM":
    print "12:00:00"
else:
    print dothething(time)