def sumnumber(numbers=None):
    numbers = [i for i in range (1, 101)] if numbers is None else numbers
    sum = 0
    for i in range (0, len(numbers)):
        sum += numbers[i]
    return sum

print (sumnumber([1,2,3]))
sumnumber(None)
sumnumber((1,2,3))
