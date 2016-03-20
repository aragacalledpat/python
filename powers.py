from math import ceil, log

def answer(s,x):
#    import pdb; pdb.set_trace()
    if s % 2 == 0 and x == 0: return 1
    if s%2 != x % 2: return 0
    if log(s+1,2).is_integer():
        if s == x:
            return x+1
        else:
            return 0

    add1 = s
    add2 = 0
    count = 0
    bottom = ceil(s/2.0)

    while add1 >= bottom:
        if add1^add2==x:
            count += 2
        add1 -= 1
        add2 += 1
    return count

assert answer(12,10) == 4
assert answer(0,0) == 1
assert answer(10,4) == 2
assert answer(5,3) == 0
assert answer(7,7) == 8


answer(100,2000000000)
print "100"
answer(1000,2000000000)
print "1000"
answer(10000,2000000000)
print "10000"
answer(100000,2000000000)
print "100000"
answer(1000000,2000000000)
print "million"
answer(10000000,2000000000)
print "10 million"
answer(100000000,2000000000)
print "100 million"
answer(1000000000,2000000000)
print "billon"
answer(2000000000,2000000000)
print "2 billon"

