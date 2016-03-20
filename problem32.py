products = []

def handle(ls):
    product = int("".join(map(str, ls[5:])))

    for x in range(1,5):
        multiplicand = int("".join(map(str,ls[:x])))
        multiplier = int("".join(map(str,ls[x:5])))
        if multiplicand * multiplier == product:
            if product not in products:
                products.append(product)


#Heap's algorithm for permutations
def generate_permutations(n,ls):
    if n == 1:
        handle(ls)
    else:
        for i in range(n - 1):
            generate_permutations(n-1,ls)
            if n % 2 == 0:
                ls[i], ls[n-1] = ls[n-1], ls[i]
            else:
                ls[0], ls[n-1] = ls[n-1], ls[0]
        generate_permutations(n-1, ls)

generate_permutations(9,[1,2,3,4,5,6,7,8,9])
print sum(products)
