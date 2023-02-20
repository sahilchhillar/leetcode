def isBadVersion(n):
    pass

def firstBadVersion(n):
    low, high = 1, n

    while low <= high:
        mid = (high+low) // 2

        if isBadVersion(mid):
            if isBadVersion(mid-1):
                high = mid-1
            else:
                return mid
        else:
            if isBadVersion(mid+1):
                return mid+1
            low = mid+1