cycles = []

def get_cycle(n):
    happened = []
    current_num = 10

    while ((current_num/n,current_num%n) not in happened) and (current_num % n != 0):
        happened.append((current_num/n,current_num % n))
        current_num = (current_num % n) * 10

    if current_num % n == 0:
        return 0
    else:
        current_tuple = (current_num/n,current_num%n)
        for i, pair in enumerate(happened):
            if current_tuple == pair:
                return len(happened[i:])


    return happened

for i in range(2,1000):
    cycles.append((i,get_cycle(i)))

cycles.sort(key=lambda x: x[1], reverse=True)

print cycles
