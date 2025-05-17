def sum(a, *args):
    #b = list(args)
    sum = 0
    for n,c in enumerate(args):
        if (n)%2 == 0:
            sum += c
    return sum

print(sum(1,100))
