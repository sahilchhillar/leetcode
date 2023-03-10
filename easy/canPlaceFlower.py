def canPlaceFlowers(flowerbed, n):
    """
    Returns True if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.
    """
    i = 0
    count = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
            flowerbed[i] = 1
            count += 1
        if count >= n:
            return True
        i += 1
    return False

print(canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))