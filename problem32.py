products = []

#Heap's algorithm for permutations
def generate(n,ls):
    if n == 1:
        print ls
    else:
        for i in range(len(ls) - 1):
            print i
            generate(n-1,ls)
            if n % 2 == 0:
                ls[i], ls[n-1] = ls[n-1], ls[i]
            else:
                ls[0], ls[n-1] = ls[n-1], ls[0]
        generate(n-1, ls)

generate(3,[5,6,7])
