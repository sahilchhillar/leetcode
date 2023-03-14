def binaryGap(n):
    pos, lastPos, count, gap = 0, 0, 0, 0
    
    while n > 0:
        bit  = n&1
        if bit == 1:
            count += 1
            if count == 1:
                lastPos = pos
            if count == 2:
                gap = max(gap, (pos-lastPos))
                count = 1
                lastPos = pos
        pos += 1
        n >>= 1
    return gap

print(binaryGap(5))