def numberOf1Bits(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        if bit == 1:
            res += 1
    return res