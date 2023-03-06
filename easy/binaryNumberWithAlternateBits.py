def binaryNumberWithAlternateBits(n):
    prev_bit = None
    while n > 0:
        curr_bit = n % 2
        if prev_bit is not None and curr_bit == prev_bit:
            return False
        prev_bit = curr_bit
        n //= 2
    return True
        
print(binaryNumberWithAlternateBits(n = 10))