def addStrings(num1, num2):
    i, j = len(num1)-1, len(num2)-1
    carry = 0
    ans = ''
    while i >= 0 and j >= 0:
        num = (ord(num1[i])-48) + (ord(num2[j])-48) + carry
        print(num)
        if num < 10:
            ans = str(num)+ans
            carry = 0
        else:
            ans = str(num%10)+ans
            carry = 1
        i -= 1
        j -= 1
    
    while i >= 0:
        num = (ord(num1[i])-48) + carry
        if num < 10:
            ans = str(num) + ans
            carry = 0
        else:
            ans = str(num%10)+ans
            carry = 1
        i -= 1
    
    while j >= 0:
        num = (ord(num2[j])-48) + carry
        if num < 10:
            ans = str(num) + ans
            carry = 0
        else:
            ans = str(num%10)+ans
            carry = 1
        j -= 1
    
    if carry:
        ans = '1'+ans
    return ans

print(addStrings(num1 = "11", num2 = "123"))