# def isPrime(num):
#     if num == 1:
#         return False
    
#     flag = True
#     for i in range(2, num):
#         if num%i == 0:
#             flag = False
#             break
#     return flag

def decToBin(num):
    count = 0
    prime = [2,3,5,7,11,13,17,19,23,29,31]
    while num > 0:
        rem = num%2
        if rem == 1:
            count += 1
        num >>= 1
    # return isPrime(count)
    return count in prime

def countPrimeSetBits(left, right):
    count = 0
    for i in range(left, right+1):
        if decToBin(i):
            count += 1
    return count

print(countPrimeSetBits(left = 10, right = 15))