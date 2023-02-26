import math

def constructRectangle(area):
    max_num = int(math.sqrt(area))
    min_diff = area-1
    length, width = 0, 0
    
    while max_num > 0:
        if area%max_num == 0:
            l = area//max_num
            w = max_num
            diff = abs(l-w)
            if diff <= min_diff:
                length = l
                width = w
                min_diff = diff
        max_num -= 1
    
    return [length, width]
    
print(constructRectangle(area = 37))    