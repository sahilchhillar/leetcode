def missingNumber(nums):
    numbers = len(nums)

    sum_all = numbers*(numbers+1)//2

    sum_nums = sum(nums)

    return sum_all - sum_nums


print(missingNumber(nums = [9,6,4,2,3,5,7,0,1]))