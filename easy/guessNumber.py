def guess(n):
    pass

def guessNumber(n):
    low, high = 1, n

    while low <= high:
        pick = (high+low)//2
        res = guess(pick)

        if res == 0:
            return pick
        elif res == -1:
            high = pick-1
        else:
            low = pick+1
    return -1