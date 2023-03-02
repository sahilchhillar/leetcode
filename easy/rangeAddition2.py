import sys

def rangeAddition(m, n, ops):
    if not ops:
        return m*n
    
    min_row = sys.maxsize
    min_col = sys.maxsize

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])
    
    return min_row*min_col

print(rangeAddition(m = 3, n = 3, ops = []))