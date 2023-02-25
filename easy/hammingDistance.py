def decToBin(c):
    count = 0
    while c > 0:
        num = c%2
        if num == 1:
            count += 1
        c >>= 1
    return count

def hammingDistance(a, b):
    c = a ^ b
    return decToBin(c)

print(hammingDistance(4, 1))