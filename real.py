def answer(s,x):
    half = s/2
    return _answer(x,(half,half,half^half),(0,s,0^s),1)

def _answer(x, bottom, top, count):
    acceptable_findings = get_acceptables(bottom[2],top[2])
    pows = get_pows(bottom,top,acceptable_findings)

def get_acceptables(bottom,top):
    power = 0
    things = []
    while bottom+(2**power) < top:
        things.append(bottom+2**power)
        power += 1
    return things

def get_pows(bottom,top,acceptable):
    #import pdb;pdb.set_trace()
    pows = []
    power = 0
    while bottom[1] + (2**power) < top[1]:
        change = 2**power
        add1 = bottom[0] - change
        add2 = bottom[1] + change
        new_val = (add1,add2,add1^add2)
        if new_val[2] in acceptable:
            pows.append(new_val)
        power += 1
    return pows

print get_acceptables(0,100)
hey = get_acceptables(0,100)
print get_pows((50,50,0), (0,100,100) ,hey)


