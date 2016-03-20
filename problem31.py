total = 200
values = [200,100,50,20,10,5,2,1]
init = [None,None,None,None,None, None, None, None]
count = 0

def sum_list(list):
    sum = 0
    for x in range(len(list)):
        if list[x] != None:
            sum += values[x] * list[x]
    return sum

def make_lists(current_list):
    next_up = []
    current_sum = sum_list(current_list)
    current_added_value = 0;

    for x in range(len(current_list)):
        if current_list[x] == None:
            index_to_change = x
            break

    if index_to_change == len(current_list) - 1:
        last_val = total - current_sum
        current_list[index_to_change] = last_val
        next_up.append(current_list[:])
        return next_up

    current_list[index_to_change] = current_added_value
    while (sum_list(current_list) <= total):
        next_up.append(current_list[:])
        current_added_value += 1
        current_list[index_to_change] = current_added_value
    return next_up

def handle_list(list):
    global count
    if sum_list(list) == total:
        count += 1
        return
    else:
        for ls in make_lists(list):
            handle_list(ls)

handle_list(init)
print count
#handle_list(init)
