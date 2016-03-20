from math import ceil

def generator(s):
    if s % 2 == 0 and x == 0: return 1

    add1=s
    add2 = 0
    if s % 2 == 0:
        bottom = s/2
    else:
        bottom = int(ceil(s/2.0))
    my_list = []
    while add1 >= bottom:
        my_list.append(add1^add2)
        add1 -= 1
        add2 += 1
    my_list.reverse()
    return my_list


for x in range(0,64):
    print generator(x)
