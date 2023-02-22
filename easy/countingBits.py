def decToBin(n):
    count = 0
    while n > 0:
        bin = n%2
        n //= 2
        if bin:
            count += 1
    return count


def countBits(n):
    ans = []
    for i in range(n+1):
        ans.append(decToBin(i))
    return ans

print(countBits(0))